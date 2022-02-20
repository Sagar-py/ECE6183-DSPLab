### demo 12
#   The past demo program play_vibrato_interpolation.py does not 
#   use blocking (it reads and writes one sample at a time). Write a 
#   version of this program that reads, processes, and writes the 
#   audio signal in blocks of 64 frames. Verify that the output 
#   signal of the new version (using block processing) is the same.


# play_vibrato_interpolation.py
# Reads a specified wave file (mono) and plays it with a vibrato effect.
# (Sinusoidally time-varying delay)
# Uses linear interpolation



import pyaudio
import wave
import struct
import math
import matplotlib

def clip16(x):
    if x>32767:
        return 32767
    elif x<-32768:
        return -32768
    else:
        return x

wavfile = 'author.wav'


print('Play the wave file: %s.' % wavfile)

# Open wave file
wf = wave.open( wavfile, 'rb')

# Read wave file properties
RATE        = wf.getframerate()     # Frame rate (frames/second)
WIDTH       = wf.getsampwidth()     # Number of bytes per sample
LEN         = wf.getnframes()       # Signal length
CHANNELS    = wf.getnchannels()     # Number of channels

print('The file has %d channel(s).'         % CHANNELS)
print('The file has %d frames/second.'      % RATE)
print('The file has %d frames.'             % LEN)
print('The file has %d bytes per sample.'   % WIDTH)

# Vibrato parameters
f0 = 2
W = 0.2   # W = 0 for no effect


# Buffer to store past signal values. Initialize to zero.
BUFFER_LEN =  1024          # Set buffer length.
buffer = BUFFER_LEN * [0]   # list of zeros

# Buffer (delay line) indices
kr = 0  # read index
kw = int(0.5 * BUFFER_LEN)  # write index (initialize to middle of buffer)

print('The buffer is %d samples long.' % BUFFER_LEN)

BLOCKLEN = 64      # Number of frames per block
# Create block (initialize to zero)


output_block = BLOCKLEN * [0]

# Number of blocks in wave file
num_blocks = int(math.floor(LEN/BLOCKLEN))
# Open an output audio stream
p = pyaudio.PyAudio()
stream = p.open(format      = pyaudio.paInt16,
                channels    = 1,
                rate        = RATE,
                input       = False,
                output      = True )

print ('-- Playing...')

# Loop through wave file 
input_bytes = wf.readframes(BLOCKLEN)
x=0
while len(input_bytes) >= BLOCKLEN * WIDTH:
    # Convert binary data to tuple of numbers    
    input_tuple = struct.unpack('h' * BLOCKLEN, input_bytes)

    # Go through block
    for k in range(0, BLOCKLEN):
        kr_prev = int(math.floor(kr))
        frac = kr - kr_prev    # 0 <= frac < 1
        kr_next = kr_prev + 1
        if kr_next == BUFFER_LEN:
            kr_next = 0

        y0 = (1-frac) * buffer[kr_prev] + frac * buffer[kr_next]
             
        # Update buffer
        buffer[kw] = input_tuple[k]
       

    # Increment read index
        kr = kr + 1 + W * math.sin( 2 * math.pi * f0 * x / RATE )
        # Note: kr is fractional (not integer!)

    # Ensure that 0 <= kr < BUFFER_LEN
        if kr >= BUFFER_LEN:
        # End of buffer. Circle back to front.
            kr = kr - BUFFER_LEN
    
    # Increment write index    
        kw = kw + 1
        if kw == BUFFER_LEN:
            # End of buffer. Circle back to front.
            kw = 0
        output_block[k] = int(clip16(y0))
        x+=1

    # Convert values to binary data
    output_bytes = struct.pack('h' * BLOCKLEN, *output_block)
    stream.write(output_bytes)
    input_bytes = wf.readframes(BLOCKLEN)

print('...Finished --')

stream.stop_stream()
stream.close()
p.terminate()
wf.close()
