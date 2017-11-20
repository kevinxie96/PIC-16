# -*- coding: utf-8 -*-
"""
Created on Mon Jun 05 12:20:20 2017

@author: kevinxie96
"""

# Challenge 1
#%%
import numpy as np
np.set_printoptions(threshold=np.inf)
from sklearn.decomposition import NMF

M=[[4,4,2,2,3,1,1],[1,5,5,2,1,4,5],[1,5,1,1,4,1,4],[5,4,3,1,1,1,2],[1,4,4,1,1,5,5],[5,5,3,5,5,1,2],[1,5,3,5,None,5,5]]

M1=[[4,4,2,2,3,1,1],[1,5,5,2,1,4,5],[1,5,1,1,4,1,4],[5,4,3,1,1,1,2],[1,4,4,1,1,5,5],[5,5,3,5,5,1,2]]
M2=[[4,4,2,2,1,1],[1,5,5,2,4,5],[1,5,1,1,1,4],[5,4,3,1,1,2],[1,4,4,1,5,5],[5,5,3,5,1,2],[1,5,3,5,5,5]]
model1 = NMF(n_components=3)
model1.fit(M1)
W2 = model1.fit_transform(M2)
H2 = model1.components_
W1 = model1.fit_transform(M1)
H1 = model1.components_
print (np.matmul(W2,H1))
# Challenge 2
#%%

# Lloyd’s algorithm
import random
import matplotlib.pyplot as plt

class lloyds(object):
    def __init__(self,N):
        X = np.array([(random.uniform(-1, 1), random.uniform(-1, 1)) for i in range(N)])
        x_hashable = map(tuple, X)
        X = set(x_hashable)
        findCenters = self.find_centers(X,7) 
        self.graph_centers(findCenters)
    def cluster_points(self,X, mu):
        clusters  = {}
    
        for x in X:
            bestmukey = min([(i, np.linalg.norm(np.subtract(x,m))) for i,m in enumerate(mu)], key=lambda t:t[1])[0]
            try:
                clusters[bestmukey].append(x)
            except KeyError:
                clusters[bestmukey] = [x]
        return clusters
     
    def reassign_centers(self,mu, clusters):
        newmu = []
        keys = sorted(clusters.keys())
        for k in keys:
            newmu.append(np.mean(clusters[k], axis = 0))
        return newmu
     
    def has_converged(self,mu, oldmu):
        return (set([tuple(a) for a in mu]) == set([tuple(a) for a in oldmu]))
     
    def find_centers(self,X, K):
        # Initialize to K random centers
        oldmu = random.sample(X, K)
        mu = random.sample(X, K)
        while not self.has_converged(mu, oldmu):
            oldmu = mu
            # assign points in X to clusters
            clusters = self.cluster_points(X, mu)
            # reassign points
            mu = self.reassign_centers(oldmu, clusters)
        return(mu, clusters)
    def graph_centers(self,findCenter):
        colors = ['b','g','r','c','m','y','k','#ff9600','#C8C8C8']
        fig = plt.figure()
        graph = fig.add_subplot(111)
        for i in range(len(findCenter[0])):
            for j in (findCenter[1][i]):
                graph.plot(j[0],j[1],color=colors[i],marker='o')
            graph.plot(findCenter[0][i][0],findCenter[0][i][1],color=colors[i],marker='*',markersize=15)


X = lloyds(100)

# Challenge 3
#%%
