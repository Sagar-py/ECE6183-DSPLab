clear

[x, Fs] = audioread('demo7-original.wav');

soundsc(x, Fs);

figure(1)
clf
plot(x)
xlabel('Time (sample)')
zoom on