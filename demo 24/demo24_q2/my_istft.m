function y = my_istft(X)
% y = my_istft(X)
% Inverse Short-time Fourier Transform with 50% overlap.
% Each block is multiplied by a cosine window.
% Input:
% X - STFT produced by 'my_stft'

% get sizes
[R, Nc] = size(X);

% make cosine window
n = (1:R) - 0.5;
window  = cos(pi*n/R-pi/2);


Y = ifft(X);        % inverse FFT of each column of X
y = zeros(1,R/2*(Nc+1));
i = 0;
for k = 1:Nc
    y(i + (1:R)) = y(i + (1:R)) + window .* Y(:,k).';
    i = i + R/2;
end
% take care of first half-block
y(1:R/2) = y(1:R/2) ./ (window(1:R/2).^2);
% take care of last half-block
y(end-R/2+(1:R/2)) = y(end-R/2+(1:R/2)) ./ (window(R/2+1:R).^2);

