import pandas as pd
import numpy as np
import modul_to_create_column as cc
from os import path

def concatenate_one_type_of_sample(column_of_track, length_of_column, folder, next_sample):
    column = np.zeros((length_of_column, 2)) 
    # check the length of the elements in column (assumption - all elements have the same length, so we check only first one)
    column_length = len(column_of_track[1])
    if column_length == 2:
        column = cc.read_sample(column_of_track, length_of_column, folder, next_sample)
    else:
        column = cc.create_note(column_of_track, length_of_column, folder, next_sample)
    column = np.array(column, dtype = 'int16')
    return column

def concatenate_all_samples_in_track(track, bpm, folder):
    nrow_track = track.shape[0]
    ncol_track = track.shape[1]
    # bit per second
    bps = bpm / 60
    # all samples have the same sample rate
    f = 44100
    next_sample = int(f // bps)
    N = next_sample * nrow_track
    list_of_samples = list()
    for k in range(ncol_track):
        column_of_track = track.loc[:, k]
        column = concatenate_one_type_of_sample(column_of_track, N, folder, next_sample)
        list_of_samples.append(column)
    return [N, list_of_samples]

def merge_all_concatenated_samples(list_of_samples):
    k = len(list_of_samples)
    # look for maximum number of rows in all samples
    num_of_rows = [None] * k
    for i in range(k):
        num_of_rows[i] = list_of_samples[i].shape[0]
    max_of_rows = max(num_of_rows)                 
    # append all arrays with zeros to have the same shape
    for i in range(k):             
        n = list_of_samples[i].shape[0]
        if n != max_of_rows:
            list_of_samples[i] = np.vstack((list_of_samples[i], np.zeros((max_of_rows - n, 2))))  
    #mix all sample into one array (average)
    sample_all = np.zeros((max_of_rows, 2))
    for i in range(k):
        sample_all += 1/k * list_of_samples[i]
    sample_all = np.array(sample_all, dtype = 'int16')
    return sample_all

def create_track(track_name, bpm, folder):
    path_to_track = path.join(folder, track_name)
    track = pd.read_csv(path_to_track, sep = ' ', header = None, dtype = str)
    raw_num_of_rows_and_list_of_samples = concatenate_all_samples_in_track(track, bpm, folder)
    raw_num_of_rows = raw_num_of_rows_and_list_of_samples[0]
    track_array = merge_all_concatenated_samples(raw_num_of_rows_and_list_of_samples[1])
    true_num_of_rows = track_array.shape[0]
    return [track_array, raw_num_of_rows, true_num_of_rows]

def take_track_names(folder):
    dir_to_song = path.join(folder, "song.txt")
    song = pd.read_csv(dir_to_song, header = None, dtype = str)
    # all unique tracks used in the song
    track_numbers = list(set(song.loc[:, 0]))
    num_of_tracks = len(track_numbers)
    name_of_track = [None] * num_of_tracks
    for i in range(num_of_tracks):
        name_of_track[i] = 'track' + track_numbers[i] + '.txt'
    return name_of_track

def create_all_track(bpm, folder):
    name_of_track = take_track_names(folder)
    # unique tracks
    num_of_tracks = len(name_of_track)
    dict_of_tracks = {}
    for i in range(num_of_tracks):
        dict_of_tracks[name_of_track[i]] = create_track(name_of_track[i], bpm, folder)
    return dict_of_tracks

