#!/usr/bin/python3

import modul_to_create_song as ms
import scipy.io.wavfile as wav
import pandas as pd
import tempfile
import zipfile
from os import path
from read_defs import read_defs

#main program
if __name__=="__main__":
    import sys
    import os
    path0 = os.getcwd()
    folder = sys.argv[1]
    #uncompressed file
    if path.isdir(path.join(path0, folder)):
    	defs = read_defs(folder)
    	bpm = defs['bpm']
    	song = ms.create_song(bpm, folder)
    	wav.write(path.join(folder, folder + '.wav'), 44100, song)
    #compressed file
    elif folder[-3:] == "zip":
    	zip = zipfile.ZipFile(folder)
    	dirpath = tempfile.mkdtemp()
    	zip.extractall(path = dirpath)
    	folder_unzip = folder[:-4]
    	path_unzip = path.join(dirpath, folder_unzip)
    	defs = read_defs(path_unzip)
    	bpm = defs['bpm']
    	song = ms.create_song(bpm, path_unzip)
    	wav.write(path.join(".", folder_unzip + '.wav'), 44100, song)
    else:
        print("Wrong directory or name of compressed file")
