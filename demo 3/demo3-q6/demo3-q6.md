# demo 3
## Question 06

Modify filter_16.py so that it produces a stereo signal with a different frequency in left and right channels. 

**Use Headphones to verify**

In the left channel- Packing sine wave of frequency 220 Hz
	x = A * sin(2 * pi * f / Fs * n)

In the right channel- Implement difference equation
	y(n) = x(n) - a1 y(n-1) - a2 y(n-2)

For coefficients, the same coefficients are used as the initial filter_16.py file. That has a frequency of 400.43 Hz

### Code Modification

	# Output from difference equation
		output_value = gain * y0

	# Sine wave computation
		x = A * sin(2 * pi * f / Fs * n)

	# Merge and pack output signals
		output_string = struct.pack(‘hh’, int(output_value),int(x))
