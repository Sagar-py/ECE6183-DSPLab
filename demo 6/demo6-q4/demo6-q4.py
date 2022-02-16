## demo 06

#   Question 04:
#   The Python demo program implements the fourth-order 
#   difference equation with 8 variables to store past values 
#   (i.e., 8 delay units). This is the the direct form 
#   implementation. But a fourth-order difference equation can be 
#   implemented using just 4 variables to store past values (i.e., 
#   4 delay units). The canonical form can be used for this purpose. 
#   See the block diagram in Fig. 7.2.4 on page 274 of the text 
#   book ‘Introduction to Signal Processing’ by Orfanidis



import pyaudio
import wave
import struct
import math

def clip16 (val):
    if val > 32767:
        return 32767
    elif val < -32768:
        return -32768
    else:
        return val

wavefile = 'author.wav'

print('Play the wave file %s.' % wavefile)

# Open wave file (should be mono channel)
wf = wave.open( wavefile, 'rb' )

# Read the wave file properties
num_channels    = wf.getnchannels()     # Number of channels
RATE            = wf.getframerate()     # Sampling rate (frames/second)
signal_length   = wf.getnframes()       # Signal length
width           = wf.getsampwidth()     # Number of bytes per sample

print('The file has %d channel(s).'            % num_channels)
print('The frame rate is %d frames/second.'    % RATE)
print('The file has %d frames.'                % signal_length)
print('There are %d bytes per sample.'         % width)

# Difference equation coefficients
b0 =  0.008442692929081
b2 = -0.016885385858161
b4 =  0.008442692929081

# a0 =  1.000000000000000
a1 = -3.580673542760982
a2 =  4.942669993770672
a3 = -3.114402101627517
a4 =  0.757546944478829

# Initialization
w1 = 0.0
w2 = 0.0
w3 = 0.0
w4 = 0.0

p = pyaudio.PyAudio()

# Open audio stream
stream = p.open(
    format      = pyaudio.paInt16,
    channels    = num_channels,
    rate        = RATE,
    input       = False,
    output      = True )

# Get first frame from wave file
input_bytes = wf.readframes(1)

while len(input_bytes) > 0:

    # Convert binary data to number
    input_tuple = struct.unpack('h', input_bytes)  # One-element tuple
    input_value = input_tuple[0]                    # Number

    # Set input to difference equation
    x0 = input_value

    # Original equation
    # y(n) = b0 x(n) + b2 x(n-2) + b4 x(n-4) - a1 y(n-1) - a2 y(n-2) - a3 y(n-3) - a4 y(n-4)

    #New Difference equation
    #DIRECT FORM 2 -. CANONICAL FORM 2
    # Difference equation implementation
    w0 = x0 - a1 * w1 - a2 * w2 - a3 * w3 - a4 * w4
    y0 = b0 * w0 + b2 * w2 + b4 * w4 

    # Delays
    w4 = w3
    w3 = w2
    w2 = w1
    w1 = w0
    

    # Compute output value
    output_value = int(clip16(y0))    # Integer in allowed range

    # Convert output value to binary data
    output_bytes = struct.pack('h', output_value)  

    # Write binary data to audio stream
    stream.write(output_bytes)                     

    # Get next frame from wave file
    input_bytes = wf.readframes(1)

print('\n- Finished')

stream.stop_stream()
stream.close()
p.terminate()
