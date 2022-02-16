%% Load wave file

[x1, Fs1] = audioread('demo6-q4-direct.wav');

N1 = length(x1);
n1 = 1:N1;
t1 = n1/Fs1;

%% Load wave file

[x2, Fs2] = audioread('demo6-q4-canonical.wav');

N2 = length(x2);
n2 = 1:N2;
t2 = n2/Fs2;

figure(1)
clf
xlabel('Time (sec)')
title('Speech signal')
zoom xon

title(sprintf('Verifying Canonical form generated file with demo generated file'))
subplot(1,2,1);
plot(t1, x1)
title('Demo File')

subplot(1,2,2);
plot(t2, x2)
title('Canonical File')