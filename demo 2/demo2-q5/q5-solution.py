### Demo 2



from struct import pack
from math import sin, pi
import wave

Fs = 8000

# Writing a mono wave file
wf = wave.open('8-bit-sine-audio.wav', 'w')

# Setting no.of channels, which is 1 here
wf.setnchannels(1)			

# Setting 1 byte per sample
wf.setsampwidth(1)

# Setting framerate
wf.setframerate(Fs)	

# Using 2^7 here, since we are using 8-bits per sample
A = 2**7 - 1.0
f = 261.6					
N = int(0.5*Fs)				

for n in range(0, N):	     
	
	x = A * sin(2*pi*f/Fs*n)
	
	byte_string = pack('B', int(x+128))
	wf.writeframesraw(byte_string)

wf.close()
