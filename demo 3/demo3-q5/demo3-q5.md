# demo 3

## Question 05 
Implement transfer function.	
	H(z) = b0 +b1 z−1 +b2 z−2/1 + a1 z−1 + a2 z−2 

** Z- Transform **

Please refer to z-transform.jpg for that


### Code Modification

	a1 = -1.9
	a2 = 0.998
	b1= -0.95
	y1 = 0.0
	y2 = 0.0
	x1 = 0.0
	gain = 10000.0
	y0 = x0 + b1 * x1 - a1 * y1 - a2 * y2

	# Delays
	y2 = y1
	y1 = y0
	x1 = x0
	# Output
	output_value = clip16(gain * y0)
	output_string = struct.pack(‘h’, int(output_value))
