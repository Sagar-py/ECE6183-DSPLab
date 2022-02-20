### demo 17

#   Question 01
#   In the demo program Tk_demo_04_slider.py, whenever the gain 
#   slider is adjusted, a clicking sound can be heard, due to the 
#   discontinuity in signal waveform due to a sudden change in 
#   amplitude. Modify this program so there is no click (no 
#   signal discontinuity).


import sys
from math import cos, pi
import pyaudio
import struct

def clip16(x):
    # Clipping for 16 bits
    if x > 32767:
        x = 32767
    elif x < -32768:
        x = -32768
    else:
        x = x
    return int(x)


if sys.version_info[0] < 3:
    # for Python 2
    import Tkinter as Tk
else:
    # for Python 3
    import tkinter as Tk


def fun_quit():
    global PLAY
    print('Finished')
    PLAY = False


Fs = 8000  # rate (samples/second)
gain = 0.2 * 2 ** 15

# Define Tkinter root
top = Tk.Tk()

# Define Tk variables
f1 = Tk.DoubleVar()
gain = Tk.DoubleVar()

# Initialize Tk variables
f1.set(200)  # f1 : frequency of sinusoid (Hz)
gain.set(0.2 * 2 ** 15)

# Define buttons
S_freq = Tk.Scale(top, label='Frequency', variable=f1, from_=100, to=400, tickinterval=100)
S_gain = Tk.Scale(top, label='Gain', variable=gain, from_=0, to=2 ** 15 - 1)
Bquit = Tk.Button(top, text='Quit', command=fun_quit)

# Place buttons
Bquit.pack(side=Tk.BOTTOM, fill=Tk.X)
S_freq.pack(side=Tk.LEFT)
S_gain.pack(side=Tk.LEFT)

# Create Pyaudio object
p = pyaudio.PyAudio()
stream = p.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=Fs,
    input=False,
    output=True,
    frames_per_buffer=128)
# specify low frames_per_buffer to reduce latency

BLOCKLEN = 256
output_block = [0 for n in range(0, BLOCKLEN)]
theta = 0
prev_gain = 0
PLAY = True

print('Start --')

while PLAY:
    top.update()
    om1 = 2.0 * pi * f1.get() / Fs
    current_gain = gain.get()
    for i in range(0, BLOCKLEN):
        difference = (current_gain - prev_gain)
        # slowly increase the gain to bring smoothness into the slider and avoid click sound
        # increase gain over time on a number of samples
        # For example: if gain was increased from 1000 to 2000, then difference is 1000
        # so increase the gain in steps of 5, so gain of 2000 comes into effect after about 200 samples have been played
        # same with decreasing the gain
        # this process helps in smoothening the gain change and avoiding the click sound
        if difference > 5:
            prev_gain = prev_gain + 5  # slowly add gain if gain has been increased using slider
        elif difference < -5:
            prev_gain = prev_gain - 5  # slowly decrease the gain if gain has been decreased using slider
        else:
            prev_gain = current_gain  # keep gain same if slider has not been changed
        output_block[i] = clip16(int(prev_gain * cos(theta)))
        theta = theta + om1
    if theta > pi:
        theta = theta - 2.0 * pi
    binary_data = struct.pack('h' * BLOCKLEN, *output_block)  # 'h' for 16 bits
    stream.write(binary_data)
print('-- Finished')

stream.stop_stream()
stream.close()
p.terminate()