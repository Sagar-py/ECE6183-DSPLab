clear

[x, Fs1] = audioread('vibrato_mono.wav');

[y,Fs2] = audioread('vibrato_blocks.wav');

N1 = length(x);
N2 = length(y);
n1 = 1:N1;
t1 = n1/Fs1;
n2 = 1:N2;
t2 = n2/Fs2;

figure(1)
clf
subplot(2,1,1);
plot(t1, x);
xlabel('Time(seconds)');
title('Vibrato');
grid on;
grid minor;
zoom xon

subplot(2,1,2);
plot(t2, y);
xlabel('Time(seconds)');
title('Vibrato with blocks');
grid on;
grid minor;
zoom xon;

z = x-y;

figure();
plot(t1,z,'LineWidth',1);
xlabel('Time (sec)');
title('Difference of the two signals');
grid on;
grid minor;
zoom xon
