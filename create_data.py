import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt

# Set random seed (for reproducibility)
np.random.seed(3)

alphbtTXT = pd.read_csv('alphabet.txt', sep = '=', header = None, index_col = None).values

br_dict = {}
for l in range(len(alphbtTXT)):
	key = alphbtTXT[l][0].strip()
	val = alphbtTXT[l][1].strip().strip('[').strip(']')
	br_dict[key] = val


def create_data(sentence = 'abcdefghijklmnopqrstuvwxyz'):
	full_braille = []
	for ltr in sentence:
		braille_seq = [ltr]

		for bit in br_dict[ltr]:

			if int(bit) == 1:
				rand_num = np.random.normal(0.75, 0.15, size=(50)).tolist()
				rand_num = [0.99 if x > 1.0 else x for x in rand_num]

				# T = np.linspace(1, 50)
				# fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2,figsize=(12, 7))

				# ax1.plot(T, rand_num, '.')
				# ax1.set_xlim(1,50)
				# ax1.set_ylim(0,1.0)
				# ax1.set_xlabel('Data point from left to right')
				# ax1.set_ylabel(r'Skin Pressure')
				# ax1.set_title('(A)')
				# plt.grid()

				rand_num.sort()

				# ax2.plot(T, rand_num, '.')
				# ax2.set_xlim(1,50)
				# ax2.set_ylim(0,1.0)
				# ax2.set_xlabel('Data point from left to right')
				# ax2.set_ylabel(r'Skin Pressure')
				# ax2.set_title('(B)')
				# plt.grid()

				to_braille = rand_num[::2]
				back = rand_num[1::2]

				# ax3.plot(T, np.append(to_braille, back), '.')
				# ax3.set_xlim(1,50)
				# ax3.set_ylim(0,1.0)
				# ax3.set_xlabel('Data point from left to right')
				# ax3.set_ylabel(r'Skin Pressure')
				# ax3.set_title('(C)')
				# plt.grid()

				back.reverse()
				to_braille.extend(back)

				# ax4.plot(T, to_braille, '.')
				# ax4.set_xlim(1,50)
				# ax4.set_ylim(0,1.0)
				# ax4.set_xlabel('Data point from left to right')
				# ax4.set_ylabel(r'Skin Pressure')
				# ax4.set_title('(D)')
				# plt.grid()
				
				# plt.tight_layout()
				# plt.savefig(f'./process.png',bbox_inches='tight', dpi=300)

				braille_seq.extend(to_braille)

			elif int(bit) == 0:
				# print(bit, '0')
				rand_num = np.random.normal(0.1, 0.05, size=(50)).tolist()
				rand_num = [0.0 if x < 0.0 else x for x in rand_num]
				to_braille = np.random.normal(0.1, 0.05, size=(50)).tolist()
				braille_seq.extend(to_braille)

		full_braille.append(braille_seq)

	pd.DataFrame(full_braille).to_csv('data_seq.csv', sep = ',', header = None, index = False)

if __name__ == "__main__":
	if len(sys.argv) > 1 :
		sentence = sys.argv[1]
		create_data(sentence)
	else: 
		create_data()