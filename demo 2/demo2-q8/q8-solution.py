### Demo 2

# Question 8:	In write_sin_01.py, can you set the number of 
#				channels to be more than 2? Use Python to generate 
#				a wav file with more than two channels, with 
#				different waveforms for each channel. Read the wav 
#				file into MATLAB and plot the individual channels 
#				(zoom in if necessary to show the waveforms). 
#				Submit your Python code, MATLAB code, comments, and 
#				MATLAB plot saved as a pdf file.

# Import the modules
from struct import pack
from math import sin, pi
import wave


Fs = 8000


# Write a stereo wave file

wf = wave.open('3-channel_sine.wav', 'w')
wf.setnchannels(3)			# three channels (stereo)
wf.setsampwidth(2)			# two bytes per sample (16 bits per sample)
wf.setframerate(Fs)			# samples per second
A = 2**15 - 1.0 			# amplitude
f1 = 261.6					# frequency in Hz 
f2 = 350.0  				# frequency 2 in Hz
f3 = 440.0					# frequency 3 in Hz
N = int(0.5*Fs)				# half-second in samples

for n in range(0, N):		# half-second loop 

	# Channel 1
	x = A * sin(2*pi*f1/Fs*n)
	byte_string = pack('h', int(x))
	# 'h' stands for 'short integer' (16 bits)
	wf.writeframes(byte_string)

	# Channel 2
	x = A * sin(2*pi*f2/Fs*n)
	byte_string = pack('h', int(x))  # concatenation
	wf.writeframes(byte_string)

	# Channel 3
	x = A * sin(2*pi*f3/Fs*n)
	byte_string = pack('h', int(x))  # concatenation
	wf.writeframes(byte_string)

wf.close()