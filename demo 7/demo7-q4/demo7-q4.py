## 	demo 07

# 	Question 04:
#	Modify the demo program mic_filter.py to process the input 
#	signal x(t) so that the output signal is: y(t) = x(t) cos(2πf0t)
#	where f0 = 400 Hz. This is amplitude modulation. The 
#	output signal y(t) should both be played to the speaker 
#	(or headphones) and saved to a wave file. What is the effect 
#	of this on the voice signal? Submit your wave (wav) file of 
#	yourself talking, as well as your code.



import pyaudio
import struct
import math
import wave


def clip16( x ):    
    # 	Clipping for 16 bits
    if x > 32767:
        x = 32767
    elif x < -32768:
        x = -32768
    else:
        x = x        
    return (x)


WIDTH       = 2         # 	Number of bytes per sample
CHANNELS    = 1         # 	Number of channels: mono
RATE        = 16000     # 	Sampling rate (frames/second)
DURATION    = 6         # 	Duration of processing (seconds)

N = DURATION * RATE     # 	N: Number of samples to process
f0 = 400
gain = 1

# 	Open audio stream
wf = wave.open('demo7-altered.wav','w')
wf.setnchannels(CHANNELS)      
wf.setsampwidth(WIDTH)
wf.setframerate(RATE)

wf2 = wave.open('demo7-original.wav','w')
wf2.setnchannels(CHANNELS)
wf2.setsampwidth(WIDTH)
wf2.setframerate(RATE)

p = pyaudio.PyAudio()

# 	Open audio stream
stream = p.open(
    format      = p.get_format_from_width(WIDTH),
    channels    = CHANNELS,
    rate        = RATE,
    input       = True,
    output      = True)

print('-- Start')

for n in range(0, N):

    # 	Get one frame from audio input (microphone)
    input_bytes = stream.read(1)

    # 	Convert binary data to tuple of numbers
    input_tuple = struct.unpack('h', input_bytes)

    # 	Convert one-element tuple to number
    x0 = input_tuple[0]

    # 	Write frame to demo_original.wav
    wf2.writeframes(struct.pack('h',int(clip16(x0))))

    # 	Difference equation
    y0 = x0 * math.cos(2 * math.pi * f0 * n * (1/RATE))

    # 	Compute output value
    output_value = int(clip16(gain* y0))    # Number

    # 	output_value = int(clip16(x0))   
    # 	Bypass filter (listen to input directly)

    # 	Convert output value to binary data
    output_bytes = struct.pack('h', output_value)  
    wf.writeframesraw(output_bytes)

    # 	Write binary data to audio stream
    stream.write(output_bytes)

print('-- Finished')
print('Length of output_bytes: ', len(output_bytes))

wf.close()
stream.stop_stream()
stream.close()
p.terminate()