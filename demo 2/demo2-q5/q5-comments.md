# Question 5: Observations

Using a sample rate of half the initial 32-bit wave and 4,000 samples per second, a sine wave was generated.
The frequency was 120 Hz.

## 5.a
Is there any noticeable effect of a lower number of bits/sample on the sound quality (keeping the same number of samples/second)?

**Answer:**

Yes, there is an observable amount of change in the quality of sound when we decrease the number of samples per signal. The 8-bit wave is not as sharp and high quality as that of the 32-bit wave.

## 5.b
If yes, then try to explain the reasons?

**Answer:**

The difference in maximum amplitude of each wave could be a factor. The 8-bit wave has a peak amplitude of 127 (which is also the Quantization of $2^7$) and thus is unable to capture the same quality as that of the 32-bit wave which has the maximum amplitude of 32,767.