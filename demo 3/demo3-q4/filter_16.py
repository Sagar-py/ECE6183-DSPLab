## demo 3
# Question 04

# filter_16.py
# 
# Implement the second-order recursive difference equation
# y(n) = x(n) - a1 y(n-1) - a2 y(n-2)
# 
# 16 bit/sample


from math import cos, pi 
import pyaudio
import struct

# Fs : Sampling frequency (samples/second)
Fs = 8000

T = 1       # T : Duration of audio to play (seconds)
N = T*Fs    # N : Number of samples to play

# Difference equation coefficients
a1 = -1.9
a2 = 0.998

# Initialization
y1 = 0.0
y2 = 0.0

## Uncomment the gain value to use

#gain = 5000.0
gain = 10000.0
#gain = 20000.0
#gain = 30000.0

p = pyaudio.PyAudio()
stream = p.open(format = pyaudio.paInt16,  
                channels = 1, 
                rate = Fs,
                input = False, 
                output = True)

# Run difference equation
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

    # Output
    output_value = gain * y0

    ###### ANSWER MODIFICATION #######
    # If else block to trap overflow of the gain value and set it to 
    # max allowed value. 

    if (output_value<=32767 and output_value>=(-32767)):
        output_string = struct.pack('h', int(output_value))   # 'h' for 16 bits
    elif output_value>0:        #if output value is positive and not in the bounds specified for 16 bits
        output_string=struct.pack('h',32767)
    else:                       #if output value is negative and not in the bounds specified for 16 bits
        output_string=struct.pack('h',-32767)

    ##### END ANSWER ######
    stream.write(output_string)

print("* Finished *")

stream.stop_stream()
stream.close()
p.terminate()
