%%  demo 08
%   For the filter implemented in the demo program, what is the difference
%   equation, the transfer function and impulse response? Use Matlab to 
%   plot the pole-zero diagram of the filter.

clear;
%%  Code

N= 800;

b=[1 zeros(1,N-1) 0.8];
a=[1 0];

figure(1);
zplane(b,a);
title('Pole-Zero plot');