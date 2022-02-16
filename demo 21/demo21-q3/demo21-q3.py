### demo 21


import pyaudio
import struct
import wave
import numpy as np
from scipy import signal
from math import pi

print('Started...')

fs = 16000          # Sampling frequency
CHANNELS = 1        # Mono channel
DURATION = 10       # 10 seconds to take input from mic
fr = 8              # Frame rate
N = fs * DURATION   # N total sample number for the specified duration
order = 7           # Complex filter

# Making a low-pass filter
# Referred demo05.m
[b_lpf, a_lpf] = signal.ellip(order, 0.2, 50, 0.48)

# Define imaginary coefficients
imaginary = 1j
x = [imaginary ** i for i in range(0, order + 1)]
a = [0 * l for l in range(0, order + 1)]
b = [0 * l for l in range(0, order + 1)]


for k in range(0, order + 1):
    b[k] = b_lpf[k] * x[k]
    a[k] = a_lpf[k] * x[k]

filter_states = np.zeros(order)

# Pyaudio object
p = pyaudio.PyAudio()
# Open a stream to read and write audio
stream = p.open(rate=fs,
                channels=CHANNELS,
                format=pyaudio.paInt16,
                input=True,
                output=True)

# Generate output wave file
wavfile = 'solution.wav'
wf = wave.open(wavfile, 'w')  

# Set mono channel
wf.setnchannels(CHANNELS)  
# Set two bytes per sample
wf.setsampwidth(2)  
# Set samples per second
wf.setframerate(fs)  


for k in range(0, int(N / fr)):
    # Read from the microphone, real-time
    string = stream.read(fr, exception_on_overflow=False)
    input_block = struct.unpack('h' * fr, string)
    # Apply filter on the read data
    output_block, states = signal.lfilter(b, a, input_block, zi=filter_states)

    # Modulation freq
    freq = 400
    # Combination of real and imaginary part
    g = [1j for i in range(0, order + 1)]
    op = [0 for i in range(0, fr)]

    for m in range(0, fr):
        # Intermediate calculation
        c = np.e ** (imaginary * 2 * pi * freq * (k * 8 + m) / fs)
        # Shift real part 2 * pi towards right
        g[m] = (output_block[m] * c).real
        # Consider real part only
        op[m] = int(g[m].real)
        output = struct.pack('h', op[m])
        # Write modulated output in a wave file
        wf.writeframesraw(output)
        stream.write(output)

# close the wave file, stop the audio stream to headphones
print("...Done")
wf.close()
stream.stop_stream()
stream.close()
p.terminate()