### demo 18

import pyaudio, struct
import numpy as np
from scipy import signal
from math import sin, cos, pi
import tkinter as Tk    

BLOCKLEN    = 64        # Number of frames per block
WIDTH       = 2         # Bytes per sample
CHANNELS    = 1         # Mono
RATE        = 8000      # Frames per second

MAXVALUE = 2**15-1      # Maximum allowed output signal value (because WIDTH = 2)


print ('Start')
# Parameters
Ta = 2      
f1 = 220    
f2 = 220 * 2 ** (1.0/12.0)
f3 = 220 * 2 ** (2.0/12.0)
f4 = 220 * 2 ** (3.0/12.0)
f5 = 220 * 2 ** (4.0/12.0)
f6 = 220 * 2 ** (5.0/12.0)
f7 = 220 * 2 ** (6.0/12.0)
f8 = 220 * 2 ** (7.0/12.0)
f9 = 220 * 2 ** (8.0/12.0)
f10 = 220 * 2 ** (9.0/12.0)
f11 = 220 * 2 ** (10.0/12.0)
f12 = 220 * 2 ** (11.0/12.0)

# Pole radius and angle
r = 0.02**(1.0/(Ta*RATE))

om1 = 2.0 * pi * float(f1)/RATE
om2 = 2.0 * pi * float(f2)/RATE
om3 = 2.0 * pi * float(f3)/RATE
om4 = 2.0 * pi * float(f4)/RATE
om5 = 2.0 * pi * float(f5)/RATE
om6 = 2.0 * pi * float(f6)/RATE
om7 = 2.0 * pi * float(f7)/RATE
om8 = 2.0 * pi * float(f8)/RATE
om9 = 2.0 * pi * float(f9)/RATE
om10 = 2.0 * pi * float(f10)/RATE
om11 = 2.0 * pi * float(f11)/RATE
om12 = 2.0 * pi * float(f12)/RATE

# Filter coefficients (second-order IIR)
a1 = [1, -2*r*cos(om1), r**2]
a2 = [1, -2*r*cos(om2), r**2]
a3 = [1, -2*r*cos(om3), r**2]
a4 = [1, -2*r*cos(om4), r**2]
a5 = [1, -2*r*cos(om5), r**2]
a6 = [1, -2*r*cos(om6), r**2]
a7 = [1, -2*r*cos(om7), r**2]
a8 = [1, -2*r*cos(om8), r**2]
a9 = [1, -2*r*cos(om9), r**2]
a10 = [1, -2*r*cos(om10), r**2]
a11 = [1, -2*r*cos(om11), r**2]
a12 = [1, -2*r*cos(om12), r**2]

b1 = [r*sin(om1)]
b2 = [r*sin(om2)]
b3 = [r*sin(om3)]
b4 = [r*sin(om4)]
b5 = [r*sin(om5)]
b6 = [r*sin(om6)]
b7 = [r*sin(om7)]
b8 = [r*sin(om8)]
b9 = [r*sin(om9)]
b10 = [r*sin(om10)]
b11 = [r*sin(om11)]
b12 = [r*sin(om12)]


ORDER = 2   # filter order


states1 = np.zeros(ORDER)
states2 = np.zeros(ORDER)
states3 = np.zeros(ORDER)
states4 = np.zeros(ORDER)
states5 = np.zeros(ORDER)
states6 = np.zeros(ORDER)
states7 = np.zeros(ORDER)
states8 = np.zeros(ORDER)
states9 = np.zeros(ORDER)
states10 = np.zeros(ORDER)
states11 = np.zeros(ORDER)
states12 = np.zeros(ORDER)

# x = np.zeros(BLOCKLEN)
x1 = np.zeros(BLOCKLEN)
x2 = np.zeros(BLOCKLEN)
x3 = np.zeros(BLOCKLEN)
x4 = np.zeros(BLOCKLEN)
x5 = np.zeros(BLOCKLEN)
x6 = np.zeros(BLOCKLEN)
x7 = np.zeros(BLOCKLEN)
x8 = np.zeros(BLOCKLEN)
x9 = np.zeros(BLOCKLEN)
x10 = np.zeros(BLOCKLEN)
x11 = np.zeros(BLOCKLEN)
x12 = np.zeros(BLOCKLEN)

# Open the audio output stream
p = pyaudio.PyAudio()
PA_FORMAT = pyaudio.paInt16
stream = p.open(
        format      = PA_FORMAT,
        channels    = CHANNELS,
        rate        = RATE,
        input       = False,
        output      = True,
        frames_per_buffer = 128)
# specify low frames_per_buffer to reduce latency

CONTINUE = True
KEYPRESS1 = False
KEYPRESS2 = False
KEYPRESS3 = False
KEYPRESS4 = False
KEYPRESS5 = False
KEYPRESS6 = False
KEYPRESS7 = False
KEYPRESS8 = False
KEYPRESS9 = False
KEYPRESS10 = False
KEYPRESS11 = False
KEYPRESS12 = False


def my_function(event):
    global CONTINUE
    global KEYPRESS1
    global KEYPRESS2
    global KEYPRESS3
    global KEYPRESS4
    global KEYPRESS5
    global KEYPRESS6
    global KEYPRESS7
    global KEYPRESS8
    global KEYPRESS9
    global KEYPRESS10
    global KEYPRESS11
    global KEYPRESS12

    global f1
    global f2
    global f3
    global f4
    global f5
    global f6
    global f7
    global f8
    global f9
    global f10
    global f11
    global f12

    global a1
    global a2
    global a3
    global a4
    global a5
    global a6
    global a7
    global a8
    global a9
    global a10
    global a11
    global a12

    global b1
    global b2
    global b2
    global b4
    global b5
    global b6
    global b7
    global b8
    global b9
    global b10
    global b11
    global b12

    global om1
    global om2
    global om3
    global om4
    global om5
    global om6
    global om7
    global om8
    global om9
    global om10
    global om11
    global om12

    print('The key pressed was: ' + event.char)
    if event.char == 'q':
      print('Quitting')
      CONTINUE = False
    # KEYPRESS = True

    if event.char == 'a':
        f1 = 220
        om1 = 2.0 * pi * float(f1)/RATE
        a1 = [1, -2*r*cos(om1), r**2]
        b1 = [r*sin(om1)]
        print('Frequency: %.2f' % 220.0)
        KEYPRESS1 = True
    #   KEYPRESS = True

    if event.char == 'w':
        f2 = 220 * 2 ** (1.0/12.0)
        om2 = 2.0 * pi * float(f2)/RATE
        a2 = [1, -2*r*cos(om2), r**2]
        b2 = [r*sin(om2)]
        print('Frequency: %.2f' % f2)
        KEYPRESS2 = True
    #   KEYPRESS = True

    if event.char == 's':
        f3 = 220 * 2 ** (2.0/12.0)
        om3 = 2.0 * pi * float(f3)/RATE
        a3 = [1, -2*r*cos(om3), r**2]
        b3 = [r*sin(om3)]
        print('Frequency: %.2f' % f3)
        KEYPRESS3 = True
    #   KEYPRESS = True

    if event.char == 'e':
        f4 = 220 * 2 ** (3.0/12.0)
        om4 = 2.0 * pi * float(f4)/RATE
        a4 = [1, -2*r*cos(om4), r**2]
        b4 = [r*sin(om4)]
        print('Frequency: %.2f' % f1)
        KEYPRESS4 = True
    #   KEYPRESS = True

    if event.char == 'd':
        f5 = 220 * 2 ** (4.0/12.0)
        om5 = 2.0 * pi * float(f5)/RATE
        a5 = [1, -2*r*cos(om5), r**2]
        b5 = [r*sin(om5)]
        print('Frequency: %.2f' % f5)
        KEYPRESS5 = True
    #   KEYPRESS = True

    if event.char == 'f':
        f6 = 220 * 2 ** (5.0/12.0)
        om6 = 2.0 * pi * float(f6)/RATE
        a6 = [1, -2*r*cos(om6), r**2]
        b6 = [r*sin(om6)]
        print('Frequency: %.2f' % f6)
        KEYPRESS6 = True
    #   KEYPRESS = True

    if event.char == 't':
        f7 = 220 * 2 ** (6.0/12.0)
        om7 = 2.0 * pi * float(f7)/RATE
        a7 = [1, -2*r*cos(om7), r**2]
        b7 = [r*sin(om7)]
        print('Frequency: %.2f' % f7)
        KEYPRESS7 = True
    #   KEYPRESS = True

    if event.char == 'g':
        f8 = 220 * 2 ** (7.0/12.0)
        om8 = 2.0 * pi * float(f8)/RATE
        a8 = [1, -2*r*cos(om8), r**2]
        b8 = [r*sin(om8)]
        print('Frequency: %.2f' % f8)
        KEYPRESS8 = True
    #   KEYPRESS = True

    if event.char == 'y':
        f9 = 220 * 2 ** (8.0/12.0)
        om9 = 2.0 * pi * float(f9)/RATE
        a9 = [1, -2*r*cos(om9), r**2]
        b9 = [r*sin(om9)]
        print('Frequency: %.2f' % f9)
        KEYPRESS9 = True
    #   KEYPRESS = True

    if event.char == 'h':
        f10 = 220 * 2 ** (9.0/12.0)
        om10 = 2.0 * pi * float(f10)/RATE
        a10 = [1, -2*r*cos(om10), r**2]
        b10 = [r*sin(om10)]
        print('Frequency: %.2f' % f10)
        KEYPRESS10 = True
    #   KEYPRESS = True

    if event.char == 'u':
        f11 = 220 * 2 ** (10.0/12.0)
        om11 = 2.0 * pi * float(f11)/RATE
        a11 = [1, -2*r*cos(om11), r**2]
        b11 = [r*sin(om11)]
        print('Frequency: %.2f' % f11)
        KEYPRESS11 = True
    #   KEYPRESS = True

    if event.char == 'j':
        f12 = 220 * 2 ** (11.0/12.0)
        om12 = 2.0 * pi * float(f12)/RATE
        a12 = [1, -2*r*cos(om12), r**2]
        b12 = [r*sin(om12)]
        print('Frequency: %.2f' % f12)
        KEYPRESS12 = True


    #   KEYPRESS = True


root = Tk.Tk()
root.bind("<Key>", my_function)

print('-- Press keys for sound')
print('-- Press "q" to quit')

while CONTINUE:
    root.update()


    if KEYPRESS1 and CONTINUE:
        x1[0] = 10000.0

    if KEYPRESS2 and CONTINUE:
        x2[0] = 10000.0

    if KEYPRESS3 and CONTINUE:
        x3[0] = 10000.0

    if KEYPRESS4 and CONTINUE:
        x4[0] = 10000.0

    if KEYPRESS5 and CONTINUE:
        x5[0] = 10000.0

    if KEYPRESS6 and CONTINUE:
        x6[0] = 10000.0

    if KEYPRESS7 and CONTINUE:
        x7[0] = 10000.0
       
    if KEYPRESS8 and CONTINUE:
        x8[0] = 10000.0
       
    if KEYPRESS9 and CONTINUE:
        x9[0] = 10000.0

    if KEYPRESS10 and CONTINUE:
        x10[0] = 10000.0
           
    if KEYPRESS11 and CONTINUE:
        x11[0] = 10000.0

    if KEYPRESS12 and CONTINUE:
        x12[0] = 10000.0


    [y1, states1] = signal.lfilter(b1, a1, x1, zi = states1)
    [y2, states2] = signal.lfilter(b2, a2, x2, zi = states2)
    [y3, states3] = signal.lfilter(b3, a3, x3, zi = states3)
    [y4, states4] = signal.lfilter(b4, a4, x4, zi = states4)
    [y5, states5] = signal.lfilter(b5, a5, x5, zi = states5)
    [y6, states6] = signal.lfilter(b6, a6, x6, zi = states6)
    [y7, states7] = signal.lfilter(b7, a7, x7, zi = states7)
    [y8, states8] = signal.lfilter(b8, a8, x8, zi = states8)
    [y9, states9] = signal.lfilter(b9, a9, x9, zi = states9)
    [y10, states10] = signal.lfilter(b10, a10, x10, zi = states10)
    [y11, states11] = signal.lfilter(b11, a11, x11, zi = states11)
    [y12, states12] = signal.lfilter(b12, a12, x12, zi = states12)

    # x[0] = 0.0    
    x1[0] = 0.0
    x2[0] = 0.0  
    x3[0] = 0.0  
    x4[0] = 0.0  
    x5[0] = 0.0  
    x6[0] = 0.0  
    x7[0] = 0.0          
    x8[0] = 0.0  
    x9[0] = 0.0  
    x10[0] = 0.0  
    x11[0] = 0.0  
    x12[0] = 0.0  

    KEYPRESS1 = False
    KEYPRESS2 = False
    KEYPRESS3 = False
    KEYPRESS4 = False
    KEYPRESS5 = False
    KEYPRESS6 = False
    KEYPRESS7 = False
    KEYPRESS8 = False
    KEYPRESS9 = False
    KEYPRESS10 = False
    KEYPRESS11 = False
    KEYPRESS12 = False


    y1 = np.clip(y1.astype(int), -MAXVALUE, MAXVALUE)     # Clipping
    y2 = np.clip(y2.astype(int), -MAXVALUE, MAXVALUE)     # Clipping
    y3 = np.clip(y3.astype(int), -MAXVALUE, MAXVALUE)     # Clipping
    y4 = np.clip(y4.astype(int), -MAXVALUE, MAXVALUE)     # Clipping
    y5 = np.clip(y5.astype(int), -MAXVALUE, MAXVALUE)     # Clipping
    y6 = np.clip(y6.astype(int), -MAXVALUE, MAXVALUE)     # Clipping
    y7 = np.clip(y7.astype(int), -MAXVALUE, MAXVALUE)     # Clipping
    y8 = np.clip(y8.astype(int), -MAXVALUE, MAXVALUE)     # Clipping
    y9 = np.clip(y9.astype(int), -MAXVALUE, MAXVALUE)     # Clipping
    y10 = np.clip(y10.astype(int), -MAXVALUE, MAXVALUE)     # Clipping
    y11 = np.clip(y11.astype(int), -MAXVALUE, MAXVALUE)     # Clipping
    y12 = np.clip(y12.astype(int), -MAXVALUE, MAXVALUE)     # Clipping

   

    ytotal = y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11 + y12
    ytotal = np.clip(ytotal.astype(int), -MAXVALUE, MAXVALUE)     # Clipping

    binary_data = struct.pack('h' * BLOCKLEN, *ytotal);    # Convert to binary binary data
    stream.write(binary_data, BLOCKLEN)

print('Done...')

# Close audio stream
stream.stop_stream()
stream.close()
p.terminate()