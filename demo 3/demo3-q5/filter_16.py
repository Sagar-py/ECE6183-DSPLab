## demo 3
## Question 05

# filter_16.py
# 
# Implement the second-order recursive difference equation
# y(n) = x(n) - a1 y(n-1) - a2 y(n-2)
# 
# 16 bit/sample

from math import cos, pi 
import pyaudio
import struct

def clip16( x ):
    # Clipping for 16 bits
    if x > 32767:
        x = 32767
    elif x < -32768:
        x = -32768
    else:
        x = x
    return (x)

# Fs : Sampling frequency (samples/second)
Fs = 8000

T = 1       # T : Duration of audio to play (seconds)
N = T*Fs    # N : Number of samples to play

# Difference equation coefficients
a1 = -1.9
a2 = 0.998
b1= -0.95


# Initialization
y1 = 0.0
y2 = 0.0
x1 = 0.0
gain = 32767

# Create an audio object and open an audio stream for output
p = pyaudio.PyAudio()
stream = p.open(format = pyaudio.paInt16,  
                channels = 1, 
                rate = Fs,
                input = False, 
                output = True)

# paInt16 is 16 bits/sample

# Run difference equation
for n in range(0, N):

    # Use impulse as input signal
    if n == 0:
        x0 = 1.0
    else:
        x0 = 0.0

    # Difference equation
    y0 = x0 + b1 * x1 - a1 * y1 - a2 * y2

    # Delays
    y2 = y1
    y1 = y0
    x1 = x0
    # Output
    output_value = clip16(gain * y0)
    output_string = struct.pack('h', int(output_value))   # 'h' for 16 bits
    stream.write(output_string)

print("* Finished *")

stream.stop_stream()
stream.close()
p.terminate()