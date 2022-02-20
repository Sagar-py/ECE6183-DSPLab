### demo 20


import pyaudio
import wave
import struct
from random import normalvariate
import numpy as np


# Signal information
RATE     = 8000
WIDTH    = 2
CHANNELS = 1

duration = 2 

MAXVALUE = 2**15-1  # Maximum allowed output signal value (because WIDTH = 2)

output_wavfile = 'solution.wav'
output_wf = wave.open(output_wavfile, 'w')      # wave file
output_wf.setframerate(RATE)
output_wf.setsampwidth(WIDTH)
output_wf.setnchannels(CHANNELS)


# Karplus-Strong paramters
K = 0.99
N = 60

a = list(np.zeros(N-1))
a.insert(0,1)
a.append(-K/2)
a.append(-K/2)
b = 1
print("Value of filters: {} {}".format(a[N], a[N+1]))


gain = 10000    # gain for using with normal distribution function

# input - standard normal distrubuted random sequence 
x = [gain*normalvariate(0,1) for i in range(N)]
xzeros = list(np.zeros(int(duration*RATE) - N))
x.extend(xzeros)

# num_samples = duration*RATE
num_samples = len(x)

# Create a buffer to store past values. Initialize to zero.
BUFFER_LEN = N+1   # N+1 is kept because we want max delay of N+1 samples
buffer = [ 0 for i in range(BUFFER_LEN) ]    


p = pyaudio.PyAudio()
stream = p.open(
    format      = pyaudio.paInt16,
    channels    = CHANNELS,
    rate        = RATE,
    input       = False,
    output      = True )

k = 0       # buffer index (circular index)
# overflowCounter = 0

print("Started...")

for i in range(num_samples):

    # Convert string to number
    input_value = x[i]

    if(k == N):
        output_value = b * input_value - a[N] * buffer[0] - a[N+1] * buffer[k]
    else:
        output_value = b * input_value - a[N] * buffer[k+1] - a[N+1] * buffer[k]

    # Update buffer
    buffer[k] = output_value

    # Increment buffer index
    k = k + 1
    if k >= BUFFER_LEN:
        # The index has reached the end of the buffer. Circle the index back to the front.
        k = 0

    output_value = np.clip(output_value, -MAXVALUE, MAXVALUE)     # Clipping
    output_string = struct.pack('h', int(output_value))

    stream.write(output_string)    

    output_wf.writeframes(output_string)

print("...Finished")

stream.stop_stream()
stream.close()
output_wf.close()
p.terminate()