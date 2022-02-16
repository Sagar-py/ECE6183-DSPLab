%%
clear

%%  Use Python to generate a wav file of a sine wave at 8 bits per sample. 
%   Read your 8 bit/sample wav file into MATLAB and plot the signal to 
%   verify that it is a sine wave (zoom in if necessary to show the 
%   waveform). Verify that the quantization step size is as expected 
%   and verify its spectrum.

%   (a) Is there any noticeable effect of a lower number of bits/sample 
%   on the sound quality (keeping the same number of samples/second)?
%   (b) If yes, then try to explain the reasons?

%   Submit (1) Python code, (2) generated 8-bits wav file, and 
%   (3) Matlab code for verifying waveform and quantization step size, 
%   and 4) written comments for answering (a) and (b).

%%  Load the 8-bit sine wave file

[x, Fs] = audioread("8-bit-sine-audio.wav");

%%  List the workspace variable(s)

whos

%%  Play the sound of the wave

soundsc(x, Fs);

%%  Plot the waveform

figure(1)
clf
plot(x)
xlabel('Time (sample)')
zoom on

%% Plot the waveform for 8-bit with respect to the actual time scale

N = length(x);
t = (1:N)/Fs;

figure(1)
clf
plot(t,x)
xlabel('Time (sample)')
zoom on

%%  Zooming in to the wave

xlim(0.1 + [0 0.050])

%%  Performing Quantization

x(100:110)'

%%  2^7 for 8 bit wave
%   Quantization step size is 2^7=128
x(100:110)' *2^7

%%  Quantization increment 1/2^7

2^7

%%  Getting the Frequency spectrum
%   Use Fast Fourier Transform (FFT)
%   Use power of 2 for FFT efficiency

N = length(x)

%   Use FFT length longer than signal length
Nfft = 2^ceil(2+log2(N))        

%%  Compute the Fourier transform 

X = fft(x, Nfft);
%   FFT index
k = 0:Nfft-1;      

figure(1)
clf
plot(k, abs(X))
xlabel('FFT index')
title('Spectrum')

%%  Center dc

X2 = fftshift(X);
k2 = -Nfft/2 : Nfft/2-1;

figure(1)
clf
plot(k2, abs(X2))
xlabel('FFT index')
title('Spectrum')

%%  Normalized frequency
%   Normalized frequency is in units of [cycles per sample]

fn = ( -Nfft/2 : Nfft/2-1 ) / Nfft;

figure(1)
clf
plot(fn, abs(X2))
xlabel('Frequency (cycles/sample)')
title('Spectrum')

%%  Frequency in Hz

f = fn * Fs;

figure(1)
clf
plot(f, abs(X2))
xlabel('Frequency (Hz)')
title('Spectrum')

zoom on

%%  Zooming in to notice the sidelobes

xlim([100 350])

%% Fourier transform in decibels (dB)

X_dB = 20*log10(abs(X2));

figure(1)
clf
plot(f, X_dB)
xlabel('Frequency (Hz)')
title('Spectrum (dB)')

xlim([0 Fs/2])
xlim([0 1000])
grid

print -dpdf -bestfit Ques-5-Spectrum