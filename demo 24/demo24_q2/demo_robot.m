

%% Load speech signal

% [x, fs] = wavread('author.wav');
[x, fs] = audioread('sp5894.wav');
N = length(x);

%% Compute STFT
R = 512;
Nfft = 512;
X = stft(x, R, Nfft);

% Set phase to zero in STFT-domain
X2 = abs(X);

% Synthesize 'robotic' speech signal
y2 = inv_stft(X2, R, N);

%%

y2 = y2/max(abs(y2));

audiowrite('author_robot.wav', y2, fs);

soundsc(y2, fs);

