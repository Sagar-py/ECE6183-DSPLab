## demo 3
## Question 06

# filter_16.py
# 
# Implement the second-order recursive difference equation
# y(n) = x(n) - a1 y(n-1) - a2 y(n-2)
# 
# 16 bit/sample



from math import sin, pi
import pyaudio
import struct


# Fs : Sampling frequency (samples/second)
Fs = 8000

######
## 1st signal is the difference equation implemented in filter_16.py ##
T = 1       # T : Duration of audio to play (seconds)
N = T*Fs    # N : Number of samples to play

## 2nd signal is a sine wave of frequency 220 Hz ##
A = 2**15 - 1.0             # amplitude of second signal
f = 220.0                   # frequency in Hz (note A3)
######

# Difference equation coefficients
a1 = -1.9
a2 = 0.998

# Initialization
y1 = 0.0
y2 = 0.0
gain = 10000.0


# Create an audio object and open an audio stream for output
p = pyaudio.PyAudio()
stream = p.open(format = pyaudio.paInt16,  
                channels = 2,
                rate = Fs,
                input = False, 
                output = True)

# Run difference equation and sine wave computation
for n in range(0, N):

    # Use impulse as input signal
    if n == 0:
        x0 = 1.0
    else:
        x0 = 0.0
    # Difference equation
    y0 = x0 - a1 * y1 - a2 * y2

    # Delays
    y2 = y1
    y1 = y0

    # Output from difference equation
    output_value = gain * y0

    # Sine wave computation
    x = A * sin(2 * pi * f / Fs * n)

    # Merge and pack output signals
    output_string = struct.pack('hh', int(output_value),int(x))

    stream.write(output_string)

print("* Finished *")

stream.stop_stream()
stream.close()
p.terminate()
