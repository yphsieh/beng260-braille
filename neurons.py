import numpy as np
import time
import pandas as pd
from Hodgkin_Huxley import HH
import matplotlib.pyplot as plt

def logistic(x):
	return 1/(1+np.exp((-1)*x))

class Neuron:
	def __init__(self, type):
		self.type = type
		self.input_signal = ''
		self.output_signal = ''
	
	def receive(self, signal):
		self.input_signal = signal

		# if self.type == 'interpreting' or self.type == 'alphabet':  print(f'{self.type} received {signal}')
	
	def transmit(self):
		cur_sig = self.output_signal
		self.output_signal = ''

		# if self.type == 'interpreting' or self.type == 'synchronizing' or self.type == 'alphabet':  print(f'The output of the {self.type} neuron: {cur_sig}')
		return cur_sig

	def type(self):
		return self.type

class PercNeuron(Neuron):
	def readHH(self):

		T, Idv, Vy = HH(self.input_signal)
		self.output_signal = Vy[:, 0]

class ReadNeuron(Neuron):
	def translate(self):
		ident = 250

		if np.max(self.input_signal[ident:2500-ident]) > 80: digitize = '1'
		else: digitize = '0'

		if np.max(self.input_signal[2500+ident:5000-ident]) > 80: digitize += '1'
		else: digitize += '0'

		self.output_signal = digitize

class SyncNeuron(Neuron):
	def __init__(self, type):
		super().__init__(type)
		self.memory = []

	def receive(self, signal):
		self.input_signal = signal
		if len(self.memory) < 3:
			self.memory.append(self.input_signal)
		else:
			print('Error in SYNC')

	def sync(self):
		new_sig = ''.join(self.memory)
		self.memory = []
		self.output_signal = new_sig
	

class AlphabetNeuron(Neuron):
	def __init__(self, type):
		super().__init__(type)
		
		alphbtTXT = pd.read_csv('alphabet.txt', sep = '=', header = None, index_col = None).values
		
		self.br_dict = {}
		for l in range(len(alphbtTXT)):
			key = alphbtTXT[l][1].strip().strip('[').strip(']')
			val = alphbtTXT[l][0].strip()
			self.br_dict[key] = [val, 0]
	
	def getLetter(self):
		brilles = self.input_signal

		try:
			self.br_dict[brilles][1] += 1
			time.sleep(1/self.br_dict[brilles][1])
			self.output_signal = self.br_dict[brilles][0]

		except:
			self.output_signal = 'Not found'

