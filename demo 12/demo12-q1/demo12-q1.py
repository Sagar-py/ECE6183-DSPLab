### demo 12

#   Question 1
#   The demo program AM_blocks_from_microphone.py shows how to 
#   read the microphone signal in blocks, apply amplitude modulation 
#   to this signal, then send the resulting signal in blocks to 
#   the output audio device. In a previous demo, we saw how to plot 
#   audio signals in real time.
#   In this exercise, modify the program AM_blocks_from_microphone.py 
#   to plot the output signal on the computer screen at the same 
#   time the output signal plays on the loudspeaker. The input signal 
#   can also be shown on the computer screen. You can use different 
#   colors for input and output signals (and/or offset the two 
#   signals) so they are more easily distinguished.



import pyaudio
import struct
import math
from matplotlib import pyplot

#f0 = 0      # Normal audio
f0 = 400    # Modulation frequency (Hz)

BLOCKLEN = 2048      # Number of frames per block
WIDTH = 2           # Number of bytes per signal value
CHANNELS = 1        # mono
RATE = 32000        # Frame rate (frames/second)
RECORD_SECONDS = 10

p = pyaudio.PyAudio()

stream = p.open(
    format      = p.get_format_from_width(WIDTH),
    channels    = CHANNELS,
    rate        = RATE,
    input       = True,
    output      = True)


output_block = BLOCKLEN * [0]

# Initialize phase
om = 2*math.pi*f0/RATE
theta = 0


pyplot.ion()           # Turn on interactive mode so plot gets updated

fig = pyplot.figure(1)
pyplot.subplot(2,1,1)
[g1] = pyplot.plot([], [])
pyplot.setp(g1, color = 'red')
g1.set_xdata(range(BLOCKLEN))
pyplot.ylim(-32000, 32000)
pyplot.xlim(0, BLOCKLEN)
pyplot.title("Output")

pyplot.subplot(2,1,2)
[g2] = pyplot.plot([], [])
g2.set_xdata(range(BLOCKLEN))
pyplot.setp(g2, color = 'blue')
pyplot.ylim(-32000, 32000)
pyplot.xlim(0, BLOCKLEN)
pyplot.xlabel('Input')


# Number of blocks to run for
num_blocks = int(RATE / BLOCKLEN * RECORD_SECONDS)

print('* Recording for %.3f seconds' % RECORD_SECONDS)

# Start loop
for i in range(0, num_blocks):

    # Get frames from audio input stream
    # input_bytes = stream.read(BLOCKLEN)       # BLOCKLEN = number of frames read
    input_bytes = stream.read(BLOCKLEN, exception_on_overflow = False)   # BLOCKLEN = number of frames read

    # Convert binary data to tuple of numbers
    input_tuple = struct.unpack('h' * BLOCKLEN, input_bytes)
   
    # Go through block
    for n in range(0, BLOCKLEN):
        # No processing:
        # output_block[n] = input_tuple[n]  
        # OR
        # Amplitude modulation:
        theta = theta + om
        output_block[n] = int( input_tuple[n] * math.cos(theta) )

    # keep theta betwen -pi and pi
    while theta > math.pi:
        theta = theta - 2*math.pi

    g1.set_ydata(output_block)
    g2.set_ydata(input_tuple)    
    pyplot.pause(0.0001)
    # Convert values to binary data
    output_bytes = struct.pack('h' * BLOCKLEN, *output_block)

    # Write binary data to audio output stream
    stream.write(output_bytes)

print('* Finished')

stream.stop_stream()
stream.close()
p.terminate()