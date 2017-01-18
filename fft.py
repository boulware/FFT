import numpy as np
import matplotlib.pyplot as plt
import wave
import scipy.fftpack
#from tkinter import *
#import tkFileDialog
#from tkFileDialog import askopenfile

def PrintWAVProperties(data):
	print("channels: 				"	+ str(data.getnchannels()))
	print("sample width (bytes): 	"	+ str(data.getsampwidth()))
	print("sampling frequency:		"	+ str(data.getframerate()))
	print("frame count:			"		+ str(data.getnframes()))
	print("compression type:		"	+ str(data.getcomptype()))

#raw_WAV = tk.askopenfile(mode='rb')

raw_WAV = wave.open('trumpet(2h).wav', 'rb')
PrintWAVProperties(raw_WAV)

f = 0.5

Fs = 48000.0
Ts = 1.0/Fs
n = int(f * raw_WAV.getnframes())
#print("n=" + str(n))
k = np.arange(n)
T = n / Fs
frq = k / T
frq = frq[range(n//2)]
#frq = frq[range(n/2)]

frames = raw_WAV.readframes(int(n))
raw_WAV.close()
signal = np.fromstring(frames, 'Int16')
#print(signal)

#for frame in frame_array_bytes:
	#frame_array_ints.append()
#print(type(frame_array_bytes))

#plt.plot(signal)
fft_signal = scipy.fftpack.fft(signal)
fft_signal = fft_signal[range(n//2)]
#print(fft_signal)
#fft_signal = np.fft.fft(signal)
#print(fft_signal)
#print(str(len(frq)) + "; " + str(len(fft_signal)))
plt.plot(frq, fft_signal)
plt.show()
#a = [0]

#np.fft.fft(np.exp(2j*np.pi*np.arange(8) / 8))