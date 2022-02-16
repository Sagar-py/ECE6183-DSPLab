%% demo 08
%   In the demo program echo_via_circular_buffer.py, change the line 
%   buffer[k] = x0 to buffer[k] = y0 and comment on how this affects the 
%   sound of the output. With this change, what is the difference 
%   equation, transfer function, and impulse response of the system?
%   What happens when the gain for the delayed value is greater than 1?

clear;
%% Code

N= 800;

a=[1 zeros(1,N-1) -0.8];
b=[1 0];


figure(2);
impz(b,a);
title('Impulse response');