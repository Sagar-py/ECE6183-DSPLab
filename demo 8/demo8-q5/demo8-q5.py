### demo 08

#	Question 05:
#	Modify the demo program so that the input audio is from microphone.

import pyaudio
#import wave
import struct


def clip16( x ):    
    #	Clipping for 16 bits
    if x > 32767:
        x = 32767
    elif x < -32768:
        x = -32768
    else:
        x = x        
    return(x)

RATE=16000

# 	Set parameters of delay system
b0 = 1.0            # 	direct-path gain
G = 0.8             # 	feed-forward gain
delay_sec = 0.1   	# 	delay in seconds, 50 milliseconds. Try delay_sec = 0.02
DURATION=6
samples=DURATION*RATE
N = int(RATE * delay_sec)   # 	delay in samples

print('The delay of {:.3f} seconds is {} samples.'.format(delay_sec, N))

# 	Buffer to store past signal values. Initialize to zero.
BUFFER_LEN = N              # 	length of buffer
buffer = BUFFER_LEN * [0]   # 	list of zeros

# 	Open an output audio stream
p = pyaudio.PyAudio()
stream = p.open(format      = pyaudio.paInt16,
                channels    = 1,
                rate        = RATE,
                input       = True,
                output      = True )

# 	Get first frame
input_bytes = stream.read(1,exception_on_overflow=False)

# 	Initialize buffer index (circular index)
k = 0

print('-- Started --')

for n in range(0,samples):

    # 	Convert binary data to number
    x0, = struct.unpack('h', input_bytes)

    # 	Compute output value
    # 	y(n) = b0 x(n) + G x(n-N)
    y0 = b0 * x0 + G * buffer[k]

    # 	Update buffer
    buffer[k] = x0

    # 	Increment buffer index
    k = k + 1
    if k >= BUFFER_LEN:
        # 	The index has reached the end of the buffer. Circle the index back to the front.
        k = 0

    # 	Clip and convert output value to binary data
    output_bytes = struct.pack('h', int(clip16(y0)))

    # 	Write output value to audio stream
    stream.write(output_bytes)

    # 	Get next frame
    input_bytes = stream.read(1,exception_on_overflow=False)

print('-- Finished --')

stream.stop_stream()
stream.close()
p.terminate()