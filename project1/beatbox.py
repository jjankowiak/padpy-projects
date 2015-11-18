#!/usr/bin/python3

import modul_to_create_song as ms
import scipy.io.wavfile as wav
import pandas as pd
from os import path
from read_defs import read_defs

if __name__=="__main__":
    import sys
    import os
    path0 = os.getcwd()
    folder = sys.argv[1]
    if path.isdir(path.join(path0, folder)):
        defs = read_defs(folder)
        bpm = defs['bpm']
        song = ms.create_song(bpm, folder)
        wav.write(path.join(folder, folder + '.wav'), 44100, song)
    else:
        print("Wrong directory")
