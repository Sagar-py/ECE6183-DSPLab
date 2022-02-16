# demo 10

**Name:** Sagar Patel

**NETID:** sp5894

---

## Question 04:
Write a Python program to implement the flanger effect. Use interpolation for an improved result. As described in Chapter 2 of Audio Effects: Theory, Implementation and Application, the flanger effect is like the vibrato effect but it additionally has a direct path, as shown in the figure. The input signal should be read from a wave file.

**Answer:**

Made a modification in the _play_vibrato_interpolation_ver2.py_ to implement the Flanger effect.

$\quad$ `gain = 0.6`	(Line 59)

$\quad$ `y0 = x0 + gain*((1-frac) * buffer[krprev] + frac*buffer[krnext])`	(Line 95)

The output is stored in the `cosine_200_hz_flanger.wav` file.
