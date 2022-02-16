### Demo 2

# Question 2: 	Write a Python script using the wav module to read 
# 				and print basic information about your wav file. 
# 				See the demo file read_wavefile_02.py. Verify that 
#				the provided information matches the intended 
# 				properties of the wave file. For your 16-bit wav 
#				file, what is the value of width returned by 
#				getsampwidth()? Submit your recorded wav file, 
#				Python code, and written comments.

# Importing the wave module
import wave


# Opening the .wav file
wf = wave.open('q2-audio.wav')

# Getting the number of channels
print("The number of channels are: ",wf.getnchannels()) 	

# Checking the sampling rate (Number of frames per second)
print("The sampling rate is: ", wf.getframerate())

# Checking the signal length
print("The signal length is: ",wf.getnframes()) 	

# Checking the signal width
print('The sample width is: ',wf.getsampwidth())


print('The value of width returned by getsamplewidth() is: ',wf.getsampwidth())
wf.close()