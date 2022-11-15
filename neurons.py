import numpy as np
import time

class Neuron:
	def __init__(self, type):
		self.type = type
		self.input_signal = ''
		self.output_signal = ''
	
	def receive(self, signal):
		self.input_signal = signal
	
	def transmit(self):
		cur_sig = self.output_signal
		self.output_signal = ''
		return cur_sig

	def type(self):
		return self.type

class ReadNeuron(Neuron):
	def denoise(self):
		## denoise input signals
		if self.input_signal >= 0.75:
			self.output_signal = '1'
		else:
			self.output_signal = '0'
		#self.output_signal = self.input_signal
		
class SyncNeuron(Neuron):
	def __init__(self, type):
		super().__init__(type)
		self.memory = ''

	def sync(self, bit1, bit2, bit3):
		new_sig = bit1 + bit2 + bit3
		
		if self.memory != '':
			for i in range(3):
				self.output_signal += (self.memory[i] + new_sig[i])
			self.memory = ''

		else:
			self.memory = new_sig
	

class AlphabetNeuron(Neuron):
	def __init__(self, type):
		super().__init__(type)
		brillesLib = ["000001", "000000", "100000", "101000", "110000", "110100", "100100", "111000", "111100", "101100", "011000", "011100", "100010", "101010", "101100", "101110", "101010", "111100", "111110", "111010", "011100", "011110", "101001", "111001", "010111", "101101", "101111", "101011"]
		asciiCodes = [True, ' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
		
		self.br_dict = {}
		for l in range(len(brillesLib)):
			self.br_dict[brillesLib[l]] = [asciiCodes[l], 0]
	
	def getLetter(self):
		brilles = self.input_signal

		try:
			self.br_dict[brilles][1] += 1
			time.sleep(1/self.br_dict[brilles][1])
			return self.br_dict[brilles][0]

		except:
			return 'Not found'

