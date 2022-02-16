# demo 05

**Name:** Sagar Patel

**NETID:** sp5894

---

## Question 01

### 1.1
**Single program for mono and stereo.** Write a single Python program to play both mono and stereo wave files. The program should determine the number of channels by reading the wave file information.

**Answer:**

Modification in code is following:


`while len(input_bytes) > 0:`

$\quad$`	if num_channels==1:`

$\quad \quad$`		input_tuple = struct.unpack('h', input_bytes)`

$\quad \quad$`		input_value = input_tuple[0]`

$\quad \quad$`		output_value = int(clip16(gain * input_value))`

$\quad$`	else:`

$\quad \quad$`		input_tuple = struct.unpack('hh', input_bytes)`

$\quad \quad$`		output_value0 = int(clip16(gain * input_tuple[0]))`

$\quad \quad$`		output_value1 = int(clip16(gain * input_tuple[1]))`


### 1.2
Verify that your program can play both mono and stereo wave files encoded with 16-bits per sample.

**Answer:**

By default, the wave file loaded is a stereo wave, `sin01_stereo.wav`. In addition to that, the script inputs one argument from the command line.

The parameter can take the value 'mono' which plays the mono channel wave, `author.wav`. The same argument can take the name of any file referenced by the path.

So basically, the two possible ways of implementing the output are:

- **`python3 demo5-q1.py`** will compile the stereo wav file `sin01_stereo.wav`
- **`python3 mono`** will execute the mono wav file
