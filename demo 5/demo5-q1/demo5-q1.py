##  demo 5

#   Question 01:
#   Single program for mono and stereo. 
#   Write a single Python program to play both mono and stereo 
#   wave files. The program should determine the number of 
#   channels by reading the wave file information. Verify that your 
#   program can play both mono and stereo wave files encoded 
#   with 16-bits per sample.

#####################################

import pyaudio
import wave
import struct
import math
import sys

def clip16( x ):    
    # Here, we will be clipping for 16 bits
    
    if x > 32767:
        x = 32767
    elif x < -32768:
        x = -32768
    else:
        x = x        
    return (x)

gain = 0.5


#   Determining the input arguments 
#   Kindly refer to the documentation file solution.pdf or solution.md

if len(sys.argv)>1:
    if sys.argv[1] == 'mono':
        #   wavefile = 'sin01_mono.wav'
        #   In order to compile this, uncomment the previous line
        wavefile = 'author.wav'
    else:
        wavefile = sys.argv[1]   
else: 
    wavefile = 'sin01_stereo.wav'

print('Play the wave file %s.' % wavefile)

#   Opening the wave file (should be mono channel)
wf = wave.open( wavefile, 'rb' )

#   Reading the wave file properties
num_channels    = wf.getnchannels()     # Get the number of channels
RATE            = wf.getframerate()     # Get the sampling rate (frames/second)
signal_length   = wf.getnframes()       # Get the signal length
width           = wf.getsampwidth()     # Get the number of bytes per sample

print('The file has %d channel(s).'            % num_channels)
print('The frame rate is %d frames/second.'    % RATE)
print('The file has %d frames.'                % signal_length)
print('There are %d bytes per sample.'         % width)

p = pyaudio.PyAudio()

#   Open audio stream
stream = p.open(
    format      = pyaudio.paInt16,
    channels    = num_channels,
    rate        = RATE,
    input       = False,
    output      = True )

#   Get first frame
input_bytes = wf.readframes(1)

while len(input_bytes) > 0:

    if num_channels == 1:
        #   Convert binary data to number
        input_tuple = struct.unpack('h', input_bytes)   #   One-element tuple (unpack produces a tuple)
        input_value = input_tuple[0]                    #   Number

        #   Compute output value
        output_value = int(clip16(gain * input_value))  # Integer in allowed range

        #   Convert output value to binary data
        output_bytes = struct.pack('h', output_value)  

        #   Get next frame
        #   input_bytes = wf.readframes(1)
    
    else:
        #   Convert binary data to numbers
        input_tuple = struct.unpack('hh', input_bytes)  # produces a two-element tuple

        #   Compute output values
        output_value0 = int(clip16(gain * input_tuple[0]))
        output_value1 = int(clip16(gain * input_tuple[1]))

        #   Convert output value to binary data
        output_bytes = struct.pack('hh', output_value0, output_value1)

    #   Write output value to audio stream
    stream.write(output_bytes)

    #   Get next frame
    input_bytes = wf.readframes(1)



if num_channels == 1:
    print('* Finished Mono *')
else:
    print('* Finished Stereo *')

stream.stop_stream()
stream.close()
p.terminate()