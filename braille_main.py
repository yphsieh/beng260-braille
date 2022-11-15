import numpy as np
import random

from neurons import *

def generate_braille(wordcnt):
	brillesLib = ["000001", "000000", "100000", "110000", "100100", "100110", "100010", "110100", "110110", "110010", "010100", "010110", "101000", "111000", "101100", "101110", "101010", "111100", "111110", "111010", "011100", "011110", "101001", "111001", "010111", "101101", "101111", "101011"]
	seq = [[],[],[]]
	for w in range(wordcnt):
		letter = brillesLib[np.random.randint(26)]
		for i in range(3): seq[i].extend([int(x) for x in letter[i*2:(i+1)*2]])
	
	# seq = np.random.randint(2, size=(3,2*wordcnt))
	# seq = np.random.rand(3,2*wordcnt)
	return seq

wordcnt = 1000
input_seq = generate_braille(wordcnt)

print(input_seq)

'''
readin_neurons = []
for i in range(3):
	readin_neurons.append(ReadNeuron('read'))
	#readin_neurons[i].receive(''.join([str(x) for x in input_seq[i]]))

syncN = SyncNeuron('sync')
alphN = AlphabetNeuron('alphbt')

for t in range(wordcnt*2):
	for i in range(3):
		readin_neurons[i].receive(input_seq[i][t])
		readin_neurons[i].denoise()
	
	syncN.sync(readin_neurons[0].transmit(), readin_neurons[1].transmit(), readin_neurons[2].transmit())
	alphN.receive(syncN.transmit())
	if t % 2: print(alphN.getLetter())
'''

