import sys 
import numpy as np
import pandas as pd
import time

from neurons import *
from create_data import *

if len(sys.argv) > 1 :
	sentence = sys.argv[1]
	create_data(sentence)
else: 
	create_data()

DF = pd.read_csv('data_seq.csv', sep = ',', header = None, index_col=0)
input_seq = []
input_ltr = []
ltr_freq = {}

for letter in DF.index:
	
	if letter in ltr_freq.keys():
		ltr_freq[letter] += 1
	else:
		ltr_freq[letter] = 0

	data = DF.loc[list(DF.index == letter),:].to_numpy()
	data = data[ltr_freq[letter]].reshape(3,-1)*10

	if len(input_seq) == 0:
		input_seq = data
	else:
		input_seq = np.append(input_seq, data, axis = 1)

	input_ltr.append(letter)


# Initialize neurons
perc_neurons = []
for i in range(3):
	perc_neurons.append(PercNeuron('perceiving'))

readN = ReadNeuron('interpreting')
syncN = SyncNeuron('synchronizing')
alphN = AlphabetNeuron('alphabet')

cnt, error = 0, 0

time_spent = []
tStart = time.time()
for ltr in range(len(input_ltr)):
	tStart_ltr = time.time()
	for i in range(3):
		perc_neurons[i].receive(input_seq[i, ltr*100:(ltr+1)*100])
		perc_neurons[i].readHH()

		readN.receive(perc_neurons[i].transmit())
		readN.translate()

		syncN.receive(readN.transmit()) # 00/01/10/11
	
	syncN.sync()

	alphN.receive(syncN.transmit())
	alphN.getLetter()
	output_ltr = alphN.transmit()

	if input_ltr[ltr].lower() != output_ltr.lower():
		error += 1

	time_diff = time.time()-tStart_ltr
	print(f'Time spent: {time_diff:4.2f} sec, Target letter: {input_ltr[ltr]}, Model output: {output_ltr}\t', 'Correct!' if input_ltr[ltr] == output_ltr else 'Wrong!')

	time_spent.append(time_diff)
	cnt += 1

tEnd = time.time()
print(f'--------\nTotal of {cnt} letters, successfully identified {cnt-error} letters, failed {error} letters in {tEnd-tStart:2.2f} seconds. Acc = {100*(cnt-error)/cnt:3.2f} %')

fig, ax1 = plt.subplots(figsize=(13, 4))
ax1.plot(np.linspace(1,len(time_spent),len(time_spent)), time_spent)
ax1.set_xticks(np.linspace(1,len(time_spent),len(time_spent)))
ax1.set_xlabel('Number of Times')
ax1.set_ylabel(r'Time (sec)')
plt.savefig(f'./time.png',bbox_inches='tight', dpi=300)
