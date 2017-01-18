import tkinter as tk
from tkinter import filedialog
import wave
import numpy as np
from collections import namedtuple
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

import scipy.fftpack

# Creates an immutable tuple to store WAV file data
WAVData = namedtuple(	'WAVData',
						['raw_data',
						'channel_count',
						'sample_width',
						'sampling_frequency',
						'frame_count',
						'compression_type'])

root = tk.Tk()
file = []

def OpenWAVFile():
	file_name = filedialog.askopenfilename()
	WAV = wave.open(file_name, 'rb')

	file 		= WAVData(	raw_data 			= np.fromstring(WAV.readframes(-1), 'Int16'), # encode raw byte data as an array of signed 16-bit integers
							channel_count 		= WAV.getnchannels(),
							sample_width 		= WAV.getsampwidth(),
							sampling_frequency 	= WAV.getframerate(),
							frame_count 		= WAV.getnframes(),
							compression_type 	= WAV.getcomptype())
	WAV.close()

	fig = Figure(figsize=(5,5), dpi=100)
	waveform_plot = fig.add_subplot(2, 1, 1)
	fft_plot = fig.add_subplot(2, 1, 2)
	k = np.arange(file.frame_count)
	t = k / file.sampling_frequency # Creates discrete array of time values for our sampling frequency
	T = file.frame_count / file.sampling_frequency # Sample length in seconds
	frq = k / T

	print(file.raw_data)
	#for b in file.raw_data:
		#print(b)
	#sub_fig.plot(t, file.raw_data)
	#sub_fig.show()
	#plt.axis([0.0, t[:0], -6000.0, 6000.0])
	#plt.plot(t, file.raw_data)
	#plt.ylim([-6000.0, 6000.0])
	#plt.show()

	fft_raw_data = scipy.fftpack.fft(file.raw_data)

	waveform_plot.plot(t, file.raw_data)
	fft_plot.plot(frq, fft_raw_data)

	canvas = FigureCanvasTkAgg(fig, master=root)
	canvas.show()
	canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

	toolbar = NavigationToolbar2TkAgg(canvas, root)
	toolbar.update()
	canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

	#canvas = FigureCanvasTkAgg(fig, master=root)

menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Open...", command=OpenWAVFile, underline=0)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

root.mainloop()
