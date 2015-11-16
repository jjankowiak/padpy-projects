import numpy as np
import pandas as pd
from os import path
from modul_to_create_tracks import create_all_track
from beatbox import bpm

def create_song(bpm, folder):
    dict_of_tracks = create_all_track(bpm, folder)
    dir_to_song = path.join(folder, "song.txt")
    song = pd.read_csv(dir_to_song, header = None, dtype = str)
    # all tracks used in the song in the order
    track_names = 'track' + song.loc[:, 0] + '.txt'
    # the length of the song = sum of raw length of every track + eventually additional ending of the last track
    length_of_song = 0
    for i, j in enumerate(track_names):
        if i != len(track_names) - 1:
            length_of_song += dict_of_tracks[j][1]
        else:
            length_of_song += dict_of_tracks[j][2]
    song = np.zeros((length_of_song, 2))
    for i, j in enumerate(track_names):
        if i == 0:
            where_to_start = 0
            raw_length_of_track = dict_of_tracks[j][1]
            true_length_of_track = dict_of_tracks[j][2]
            song[where_to_start:true_length_of_track, :] += 0.5 * dict_of_tracks[j][0]
            where_to_start += raw_length_of_track 
        else:
            raw_length_of_track_new = dict_of_tracks[j][1]
            true_length_of_track_new = dict_of_tracks[j][2]
            song[where_to_start:(where_to_start + true_length_of_track_new), :] += 0.5 * dict_of_tracks[j][0]
            where_to_start += raw_length_of_track_new
    song = np.array(song, dtype = 'int16')
    return song