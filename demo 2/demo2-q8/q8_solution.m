%%
clear

%%  In write_sin_01.py, can you set the number of channels to be more 
%   than 2? Use Python to generate a wav file with more than two channels, 
%   with different waveforms for each channel. Read the wav file into 
%   MATLAB and plot the individual channels (zoom in if necessary to show 
%   the waveforms). Submit your Python code, MATLAB code, comments, 
%   and MATLAB plot saved as a pdf file.

%%  Read 3 channel wave file

[x, Fs] = audioread('3-channel_sine.wav');

%%  Calculate time axis

N = length(x);
t = (1:N)/Fs;

%%  Create subplots for the three channels

figure(1)
subplot(3,1,1)
plot(t, x(:,1))
title("261 Hz")
grid

subplot(3,1,2)
plot(t, x(:,2))
title("350 Hz")
grid

subplot(3,1,3)
plot(t, x(:,3))
title("440 Hz")
grid