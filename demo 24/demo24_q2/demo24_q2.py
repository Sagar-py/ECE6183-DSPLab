import pyaudio, wave, struct, math
import numpy as np

#source file
wavefile = 'author.wav'

print('Play the wave file %s.' % wavefile)

# Open wave file (should be mono channel)
wf = wave.open( wavefile, 'rb' )

# Read the wave file properties
num_channels    = wf.getnchannels()     # Number of channels
RATE            = wf.getframerate()     # Sampling rate (frames/second)
signal_length   = wf.getnframes()       # Signal length
WIDTH           = wf.getsampwidth()     # Number of bytes per sample

print('The file has %d channel(s).'            % num_channels)
print('The frame rate is %d frames/second.'    % RATE)
print('The file has %d frames.'                % signal_length)
print('There are %d bytes per sample.'         % WIDTH)

p = pyaudio.PyAudio()

# Open audio stream
stream = p.open(
    format      = pyaudio.paInt16,
    channels    = num_channels,
    rate        = RATE,
    input       = False,
    output      = True )

#Max value and blocklength
BLOCKLEN = 64
MAXVALUE = 2**15-1  # Maximum allowed output signal value (because WIDTH = 2)

# Get first set of frame from wave file
input_bytes = wf.readframes(BLOCKLEN)

while len(input_bytes) == WIDTH*BLOCKLEN:
    # convert binary data to numbers
    input_block = struct.unpack('h' * BLOCKLEN, input_bytes) 

    x = np.fft.rfft(input_block)
    output_block = np.fft.irfft(x)

    # Typecasting to integer
    output_block = output_block.astype(int)

    # Convert output value to binary data
    binary_data = struct.pack('h' * BLOCKLEN, *output_block)

    # Write binary data to audio stream
    stream.write(binary_data)

    # Get next frame from wave file
    input_bytes = wf.readframes(BLOCKLEN)

      
print('* Finished *')

stream.stop_stream()
stream.close()
p.terminate()