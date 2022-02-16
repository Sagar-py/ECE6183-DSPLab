%%  Question 2- Matlab GUI
%   Matlab Graphical User Interface (GUI). Write a Matlab GUI that allows 
%   the user to control the cut-off frequency of a low-pass filter. The 
%   GUI should have a slider for the cut-off frequency. The GUI 
%   should display the impulse response and the frequency response 
%   (magnitude)

%   Input File: cat01.wav

%%  Read Audio file

clear

[x,Fs]=audioread('cat01.wav')

%%  Create 2 plots
%   1.Frequency Response vs Frequency
%   2.Impulse Response vs Time


%   Make a filter

fc = 0.1;
[b, a] = butter(2, 2*fc);       
y = filtfilt(b, a, x);

%%  Calculate frequency and impulse response


%   Impulse

L = 150;
imp= [1 zeros(1,L-1)];
h=filter(b,a,imp);
h1=(0:L-1)/Fs;


%   Frequency

[H, om] = freqz(b, a);
freq = om/(2*pi);

%%  Draw figure with 2 subplots: One for frequency, One for impulse

figure(1)
title(sprintf('MATLAB GUI- DEMO 04'))
clf
subplot(1,2,1);
impulse_response_handle = plot((1:L),h1);
title('Impulse Response')

subplot(1,2,2);
frequency_response_handle = plot(freq,abs(H));
title('Frequency Response')
drawnow;

slider = uicontrol('Style','slider',...
            'Min',0.01,'Max',0.49,...
            'Value',0.125,...
            'Position',[100 10 200 15],...
            'SliderStep',[0.01 0.10],...
            'Callback',{@sliderfunction,impulse_response_handle,imp,frequency_response_handle,Fs});  

%%  Slider callback

function [] = sliderfunction(hObject,eventdata,handle_impulse,imp,handle_freq,Fs)
    
    fc = get(hObject,'value');
    
    [b, a] = butter(2,2*fc);
    h=filter(b,a,imp);
    %   h1=(0:L-1)/Fs;
    
    [H, om] = freqz(b,a);
    f = om*Fs/ (2*pi);
    
    figure(1)
    title(sprintf('Demo 04: MATLAB GUI'))
    subplot(1,2,1);
    title('Impulse Response')

    subplot(1,2,2);
    title('Frequency Response')

    set(handle_impulse,'Ydata',h);
    set(handle_freq,'Xdata',f);
    set(handle_freq,'Ydata',abs(H));
end