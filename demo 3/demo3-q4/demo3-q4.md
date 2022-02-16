# demo 3

## Question 04 
Modify  filter_16.py  to avoid run-time overflow errors even if gain is very high, by clipping the signal as necessary. To do this, insert an if statement to verify that the sample value is in the allowed range. If it is not, then set the value to its maximum (positive or negative) allowed value, before writing it to the audio stream. Test your program by setting the gain to a high value. What effect does this have on the sound produced by the program? 

### Code Modification

	# If else block to trap overflow of the gain value and set it to 
	# max allowed value. 

	if (output_value<=32767 and output_value>=(-32767)):
        output_string = struct.pack('h', int(output_value))       
	elif output_value>0:
       	output_string=struct.pack('h',32767)
    else:
        output_string=struct.pack('h',-32767)

    
## Test your program by setting the gain to a high value. What effect does this have on the sound produced by the program? 

**Answer:**

Keeping all other parameters the and increasing gain value beyond ~15000 ,the sound produced is the same for all values as the output string is refactored to the maximum value allowed by 4 bytes of data (32768, (-) 32768).