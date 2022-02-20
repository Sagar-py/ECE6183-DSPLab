%% stft_demo_1: The STFT and its inversion 
%
% This demo shows the computation of the STFT and its inverse
% using 50 percent overlapping.
%
%  Ivan Selesnick. NYU.

%% Load and plot signal
% Load the wav file using wavread (or audioread).

% [s, fs] = wavread('sp1.wav');
[s, fs] = audioread('sp5894.wav');

x = s(1:18944)';    % 73 blocks of length 512 with 50 percent overlap

N = length(x);

figure(1), clf
plot((1:N)/fs, x)
title('Speech signal')
xlabel('Time (seconds)')

%% Play audio signal
% We can listen to the signal with the soundsc command.

soundsc(x, fs);     % Play the audio file

%% Forward STFT (50 percent overlap, no window)
% Here we compute the STFT using 50 percent overlap.
% For simplicity, we use no window.
% The STFT can be computed using the loop below.
% We use a block length of 512 samples here.

R = 512;
Nb = floor(2*N/R)-1;        % Number of blocks (number of columns of X)
X = zeros(R, Nb);
i = 0;
for k = 1:Nb
    X(:,k) = x(i + (1:R));
    i = i + R/2;
end
X = fft(X);                  % Compute the FFT of each block
Tr = R/fs;                   % Duration of each block (in seconds)

%% Display spectrogram
% We display the STFT using the imagesc function.
% Both positive and negative frequencies are shown.
% (Negative frequencies are from 8000 to 16000 Hz.)

imagesc([0 N/fs], [0 fs], abs(X)); 
cmap = flipud(gray);
colormap(cmap);
axis xy 
xlabel('Time (sec.)') 
ylabel('Frequency (Hz)') 
title('Spectrogram') 
colorbar

%%
% Display the STFT for frequencies up to fs/2.
% A lot of the display is white because many of the STFT
% values are small.

imagesc([0 N/fs], [0 fs], abs(X)); 
ylim([0 fs/2])
% cmap = flipud(gray);
% colormap(cmap);
colormap('jet');
% caxis([0 20])
axis xy 
xlabel('Time (sec.)') 
ylabel('Frequency (Hz)') 
title('Spectrogram') 
colorbar

%%
% Show in dB to make small values more visible.

imagesc([0 N/fs], [0 fs], 20*log10(abs(X))); 
ylim([0 fs/2])
colormap('jet');
colorbar
axis xy 
xlabel('Time (sec.)') 
ylabel('Frequency (Hz)') 
title('Spectrogram') 
caxis([-20 30])
    
%% Inverse STFT  (50 percent overlap, no window)
% This code shows how to invert the STFT. If correct, 
% we should recover the original speech signal.
% To verify the correctness of the STFT inverse,
% the difference between the original and reconstructed
% speech signals is shown below. As seen in the graph,
% the error is less than 10^(-16), that is zero to computer
% precision.
% Note that the first and last half-block of the inverse STFT
% require their own normalization due to the absence
% of over-lapped blocks.

Y = ifft(X);        % inverse FFT of each column of X
y = zeros(size(x));
i = 0;
for k = 1:Nb
    y(i + (1:R)) = y(i + (1:R)) + 0.5*Y(:, k).';
    i = i + R/2;
end
% Take care of first half-block and last half-block
% . . . (how?)

% Display difference signal to verify perfect reconstruction
plot((1:N)/fs, x-y)
title('Reconstruction error')
xlabel('Time (sec.)') 
xlim([0 N/fs])

% The inverse is correct, except for the first half-block and
% the last half-block.

%% Window for the STFT
% When computing the STFT, it is better to multiply each block
% by a window. That will avoid discontinuities at the block
% boundaries in the reconstructed signal when the STFT coefficients
% are processed (e.g., quantized or thresholded).
% If the same window is used in both forward and inverse STFT,
% then the window should satisfy a specific
% property so that the STFT is invertible.
% One window satisfying that property is the half-cycle sine window
% shown here.

% half-cycle sine window
n = (1:R) - 0.5;
w  = sin(pi*n/R);

plot(w)
xlim([0 R])
title('Half-cycle sine window')
xlabel('n')

%% Verify the window 
% This code verifies that the window satisfies the 
% perfect reconstruction (PR) property:
% w(n)^2 + w(n+R/2)^2 = 1.
% We need verify this for n = 0, ..., R/2-1.
% The plot here shows that the sine window satisfies this condition.

% Verify that the window satisfies the required conditions
pr = w(1:R/2).^2 + w(R/2+(1:R/2)).^2;

% For perfect reconstruction 'pr' should be equal to 1.
plot(pr)
title('Verify perfect reconstruction property')
ylim([0 1.2])
xlim([1 R/2])

%% Forward STFT using a window (50 percent overlap)
% This code shows the computation of the STFT using the
% sine window. Each block is multiplied point-by-point
% with the window.

N = length(x);
Nb = floor(2*N/R)-1        % Number of blocks (columns of X)
X = zeros(R, Nb);
i = 0;
for k = 1:Nb
    X(:,k) = w .* x(i + (1:R));   % multiply signal by window
    i = i + R/2;
end
X = fft(X);                  % Compute the FFT of each block

% Display STFT
imagesc([0 N/fs], [0 fs], 20*log10(abs(X))); 
ylim([0 fs/2])
colormap('jet');
% colormap(cmap);
caxis([-20 30])
colorbar
axis xy
xlabel('Time (sec.)') 
ylabel('Frequency (Hz)') 
title('Spectrogram') 

%% Inverse STFT using a window (50 percent overlap)
% This code shows the inverse STFT. After the inverse FFT,
% each block is again multiplied point-by-point with the window.
% Note that the first and last half-block require
% separate treatment because of the absence of overlapping
% for those half-blocks.

Y = ifft(X);        % inverse FFT of each column of X
y = zeros(size(x));
i = 0;
for k = 1:Nb
    y(i + (1:R)) = y(i + (1:R)) + w .* Y(:,k).';
    i = i + R/2;
end
% Take care of first half-block and last half-block
% . . . (how?)

% Display difference signal to verify perfect reconstruction
plot((1:N)/fs, x-y)
title('Reconstruction error')
xlabel('Time (sec.)')

% The inverse is correct, except for the first half-block and
% the last half-block.

%% Using a function for STFT
% For convenience, we write functions for the STFT and inverse STFT.
% This code illustrates the perfect reconstruction property
% of my STFT and inverse STFT functions.
% My STFT and inverse STFT functions use the half-cycle sine window.

% [s, fs] = wavread('sp1.wav');
[s, fs] = audioread('sp1.wav');
N = 20000;
x = s(1:N)';
R = 512;
X = my_stft(x,R);     % function for STFT
y = my_istft(X);      % function for inverse STFT
err = x - y(1:N);
ME = max(abs(err))

% display STFT
imagesc([0 N/fs], [0 fs], 20*log10(abs(X))); 
ylim([0 fs/2])
colormap(cmap);
caxis([-20 30])
colorbar
axis xy 
xlabel('Time (sec.)') 
ylabel('Frequency (Hz)') 
title('Spectrogram') 

