import scipy.io.wavfile as wav
from os import path
import numpy as np

def read_sample(column_of_track, length_of_column, folder, next_sample):
	"""
	Function creates array which represents one column in track file which consists of two signs.
	"""
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

def create_frequency(note_string):
	"""
	Function to create frequency which responses the note name.
	"""
	letter = note_string[0]
	sharp = note_string[1]
	number = int(note_string[2])
	f_basic = 440
	S = 2 ** (1 / 12)
	# dictionary with powers
	dict_of_sound = {'A': 0, 'B': 2, 'C' : 3, 'D' : 5, 'E' : 7, 'F' : 8, 'G' : 10}
	f = f_basic * (S ** dict_of_sound[letter])
	if sharp == '#':
		f *= S
	diff_number = number - 4
	f *= 2 ** diff_number
	return f 

def create_note(column_of_track, length_of_column, folder, next_sample):
	"""
	Function creates array which represents note (sound with given frequency)
	"""
	column = np.zeros((length_of_column, 2))
	for i, j in enumerate(column_of_track):
		if j != '---':
			note_string = j
			f = create_frequency(note_string)
			t = np.linspace(0, 1, next_sample)
			y = np.sin(2 * np.pi * f * t)
			y = np.int16(y / max(np.abs(y)) * 32767)
			sample = np.transpose(np.vstack((y, y)))
			column[i * next_sample : i * next_sample + next_sample, :] += sample
	return column

	

