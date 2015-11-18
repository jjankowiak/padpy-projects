import scipy.io.wavfile as wav
from os import path
import numpy as np

def read_sample(column_of_track, length_of_column, folder, next_sample):
	# check the number of sample (only one type in one column)
    num_of_sample = list(set(column_of_track).difference(['--']))[0]
    sample = wav.read(path.join(folder, 'sample' + num_of_sample + '.wav'))
    # number of bits in the sample
    n = sample[1].shape[0]
    # if length of sample is bigger than number of sounds (?) per bit we add more columns at the end of array
    if n > next_sample:
        how_many_to_add = n - next_sample
    else:
    	how_many_to_add = 0
    column = np.zeros((length_of_column + how_many_to_add, 2))
    # concatenate sample and 'empty sounds' in order
    for i, j in enumerate(column_of_track):
        if j != '--':
            column[i * next_sample : i * next_sample + n, :] += sample[1]
    return column

def create_note(column_of_track, length_of_column, folder, next_sample):
 	print('to jeszcze trzeba dokończyć')