#!/home/justyna/anaconda3/bin/python3

import numpy as np
import pandas as pd
import os.path as op
import time 

import sklearn.cluster as cl
from sklearn.neighbors import kneighbors_graph
from sklearn.preprocessing import StandardScaler
import Levenshtein
from scipy.spatial.distance import hamming

def FM(labels, labels_predicted):
    """
    Count Fowlkes-Mallows index
    """
    df = pd.DataFrame(data = {"labels": labels, "labels_predicted": labels_predicted})
    table = df.groupby(["labels", "labels_predicted"]).size()
    table1 = df.groupby("labels").size()
    table2 = df.groupby("labels_predicted").size()
    n = len(labels)
    T = (table**2).sum() - n
    P = (table1**2).sum() - n
    Q = (table2**2).sum() - n
    B = T/np.sqrt(P*Q)
    return B

def predict_labels(X, y):
    """
    Clustering algorithms implementation
    """
    n_labels = len(np.unique(y))
    
    X = StandardScaler().fit_transform(X)
    
    ### kmeans
    # kmeans++
    kmeans_k = cl.KMeans(init = 'k-means++', n_clusters = n_labels)
    
    # random
    kmeans_r = cl.KMeans(init = 'random', n_clusters = n_labels)

    ### birch
    birch = cl.Birch(n_clusters = n_labels)
    
    ### minibatch
    minibatch = cl.MiniBatchKMeans(n_clusters = n_labels)
    
    ### spectral
    # kmeans
    spectral_k = cl.SpectralClustering(n_clusters = n_labels, eigen_solver = 'arpack',
                                     affinity = "nearest_neighbors", assign_labels = 'kmeans')
    
    # discretize
    spectral_d = cl.SpectralClustering(n_clusters = n_labels, eigen_solver = 'arpack',
                                     affinity = "nearest_neighbors", assign_labels = 'discretize')
    
    ### agglomerative
    # Ward linkage
    connectivity = kneighbors_graph(X, n_neighbors = 10, include_self = False)
    connectivity = 0.5 * (connectivity + connectivity.T)
    agg_w = cl.AgglomerativeClustering(n_clusters = n_labels, linkage = 'ward', connectivity = connectivity)
    
    # complete linkage
    agg_cl = cl.AgglomerativeClustering(
        linkage = "complete", affinity = "cityblock", n_clusters = n_labels,
        connectivity = connectivity)
    
    # avarage linkage
    agg_al = cl.AgglomerativeClustering(
        linkage = "average", affinity = "cityblock", n_clusters = n_labels,
        connectivity = connectivity)
    
    names = ["KMeans, init = 'kmeans++'", "KMeans, init = 'random'", "Birch", "MiniBatchKMeans", 
            "SpectralClustering, assign_labels = 'kmeans'", "SpectralClustering, assign_labels = 'discretize'",
            "AgglomerativeClustering, linkage = 'ward'", "AgglomerativeClustering, linkage = 'complete'",
            "AgglomerativeClustering, linkage = 'avarage'"]
    algorithms = [kmeans_k, kmeans_r, birch, minibatch, spectral_k, spectral_d, agg_w, agg_cl, agg_al]
    results = [None] * len(algorithms)
    
    for i, a in enumerate(algorithms):
        print("    Counting " + names[i])
        t0 = time.time()
        a.fit(X)
        t1 = time.time()
        run_time = t1 - t0
        if hasattr(a, 'labels_'):
            y_pred = a.labels_.astype(np.int)
        else:
            y_pred = a.predict(X)
        fm = FM(y, y_pred)
        results[i] = (run_time, fm, y_pred)
    return results


def load_data(data_name, dir_to_data):
    """
    Reading data (also transforming string and binary data to appropriate shape)
    """
    if data_name in ["actg1", "actg2", "actg3"]:
        data = np.genfromtxt(op.join(dir_to_data, data_name + ".data.gz"), dtype = 'str')
        N = len(data)
        data_input = np.zeros((N, N))
        for i in range(N):
            for j in range(N):
                data_input[i][j] = Levenshtein.distance(data[i], data[j])
    elif data_name in ["binstr1", "binstr2", "binstr3"]:
        data = np.genfromtxt(op.join(dir_to_data, data_name + ".data.gz"), dtype = 'str')
        N = len(data)
        data_input = np.zeros((N, N))
        for i in range(N):
            for j in range(N):
                data_input[i][j] = hamming(list(data[i]), list(data[j]))
    else:
        data_input = np.loadtxt(op.join(dir_to_data, data_name + ".data.gz"), ndmin = 2)
    labels = np.loadtxt(op.join(dir_to_data, data_name + ".labels.gz"), dtype = 'int')
    return (data_input, labels)


def summary_all(dir_to_data, data_names):
    """ 
    Reading data, predicting labels and counting FM index
    """
    results_all = [None] * len(data_names)
    for i, name in enumerate(data_names):
        print("Data set " + name)
        data, labels = load_data(name, dir_to_data)
        if name in ["digits2k_pixels"]:
            data = data / 255.0
        result = predict_labels(data, labels)
        results_all[i] = result
    return results_all


def save_results(results_all, data_names, algorithms_names):
    """
    Save result to csv files (two files containing tables with time and FM index and files with predicted labels (maybe they will be used earlier to compare exactly the results)).
    """
    n_datasets = len(data_names)
    n_algorithms = len(algorithms_names)
    results_time = np.zeros((n_datasets, n_algorithms))
    results_fm = results_time.copy()
    print("Saving data to csv files.")
    for i in range(n_datasets):
        results_labels = [None] * n_algorithms
        for j in range(n_algorithms):
            time = results_all[i][j][0]
            results_time[i][j] = time
            fm = results_all[i][j][1]
            results_fm[i][j] = fm
            labels = results_all[i][j][2]
            results_labels[j] = labels
        results_labels_pd = pd.DataFrame(data = results_labels, index = algorithms_names)
        results_labels_pd = results_labels_pd.transpose()
        results_labels_pd.to_csv("labels_" + data_names[i] + ".csv", header = True, index = False)
    results_time_pd = pd.DataFrame(data = results_time, index = data_names, columns = algorithms_names)
    results_time_pd.to_csv("benchmark_time.csv")
    results_fm_pd = pd.DataFrame(data = results_fm, index = data_names, columns = algorithms_names)
    results_fm_pd.to_csv("benchmark_fm.csv")
    print("Done.")


dir_to_data = "data"
data_names = ["digits2k_pixels", "iris", "iris5", "s1", "s2", "s3", "s4", "a1", "a2", "a3",
             "g2-2-100", "g2-16-100", "g2-64-100", "unbalance", "Aggregation", "Compound", "pathbased", 
             "spiral", "D31", "R15", "flame", "jain", "actg1", "actg2", "actg3", "binstr1", "binstr2", "binstr3"]
algorithms_names = ["kmeans_k", "kmeans_r", "birch", "minibatch", "spectral_k", "spectral_d", 
                    "agg_w", "agg_cl", "agg_al"]

results_all = summary_all(dir_to_data, data_names)
save_results(results_all, data_names, algorithms_names)
