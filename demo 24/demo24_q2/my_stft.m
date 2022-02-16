function X = my_stft(x,R)
% X = my_stft(x,R)
% Short-time Fourier Transform with 50% overlap.
% Each block is multiplied by a cosine window.
% Input:
% x - 1D signal
% R - block length
%
% % Example:
% [s,fs] = audioread('sp1.wav');
% Nx = 20000;
% x = s(1:Nx)';  
% R = 512;
% X = my_stft(x,R);
% y = my_istft(X);
% err = x - y(1:Nx);
% max(abs(err))

x = x(:).';  % Ensure that x is a row vector.

% cosine window
n = (1:R) - 0.5;
window  = cos(pi*n/R-pi/2);

Nx = length(x);
Nc = ceil(2*Nx/R)-1;        % Number of blocks (cols of X)
L = R/2 * (Nc + 1);
if Nx < L
    x = [x zeros(1,L-Nx)];  % zero pad x as necessary 
end
X = zeros(R,Nc);
i = 0;
for k = 1:Nc
    X(:,k) = window .* x(i + (1:R));   % multiply signal by window
    i = i + R/2;
end
X = fft(X);

