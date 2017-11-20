#==============================================================================
# # -*- coding: utf-8 -*-
# """
# Created on Wed Jun  7 18:51:29 2017
# 
# @author: kevin_000
# """
# import numpy as np
# 
# from matplotlib import pyplot as plt
# from matplotlib.collections import LineCollection
# 
# from sklearn import manifold
# from sklearn.metrics import euclidean_distances
# from sklearn.decomposition import PCA
# 
# n_samples = 50
# seed = np.random.RandomState(seed=3)
# X_true = seed.randint(0, 10, 2 * n_samples).astype(np.float)
# X_true = X_true.reshape((n_samples, 2))
# # Center the data
# X_true -= X_true.mean()
# similarities = euclidean_distances(X_true)
# # Add noise to the similarities
# noise = np.random.rand(n_samples, n_samples)
# noise = noise + noise.T
# noise[np.arange(noise.shape[0]), np.arange(noise.shape[0])] = 0
# similarities += noise
# 
# mds = manifold.MDS(n_components=2, max_iter=3000, eps=1e-9, random_state=seed,
#                    dissimilarity="precomputed", n_jobs=1)
# pos = mds.fit(similarities).embedding_
# 
# nmds = manifold.MDS(n_components=2, metric=False, max_iter=3000, eps=1e-12,
#                     dissimilarity="precomputed", random_state=seed, n_jobs=1,
#                     n_init=1)
# npos = nmds.fit_transform(similarities, init=pos)
# 
# # Rescale the data
# pos *= np.sqrt((X_true ** 2).sum()) / np.sqrt((pos ** 2).sum())
# npos *= np.sqrt((X_true ** 2).sum()) / np.sqrt((npos ** 2).sum())
# 
# # Rotate the data
# clf = PCA(n_components=2)
# X_true = clf.fit_transform(X_true)
# 
# pos = clf.fit_transform(pos)
# 
# npos = clf.fit_transform(npos)
# 
# fig = plt.figure(1)
# ax = plt.axes([0., 0., 1., 1.])
# 
# s = 100
# plt.scatter(X_true[:, 0], X_true[:, 1], color='navy', s=s, lw=0,
#             label='True Position')
# plt.scatter(pos[:, 0], pos[:, 1], color='turquoise', s=s, lw=0, label='MDS')
# plt.scatter(npos[:, 0], npos[:, 1], color='darkorange', s=s, lw=0, label='NMDS')
# plt.legend(scatterpoints=1, loc='best', shadow=False)
# 
# similarities = similarities.max() / similarities * 100
# similarities[np.isinf(similarities)] = 0
# 
# # Plot the edges
# start_idx, end_idx = np.where(pos)
# # a sequence of (*line0*, *line1*, *line2*), where::
# #            linen = (x0, y0), (x1, y1), ... (xm, ym)
# segments = [[X_true[i, :], X_true[j, :]]
#             for i in range(int(len(pos)/2)) for j in range(int(len(pos)/2))]
# values = np.abs(similarities)
# lc = LineCollection(segments,
#                     zorder=0, cmap=plt.cm.Blues,
#                     norm=plt.Normalize(0, values.max()))
# lc.set_array(similarities.flatten())
# lc.set_linewidths(0.5 * np.ones(len(segments)))
# ax.add_collection(lc)
# 
# plt.show()
#==============================================================================
list1 = [1,20,3,5.4,5,6,7.5,8.4,20,3,5.4,5,6,7.5,8.4,20,3,5.4,5,6,7.5,8.4]
#==============================================================================
# list1.sort()
# list1 = list1[::-1]
# print (list1[:10])
#==============================================================================
list1.remove(20)
print (list1)
#==============================================================================
# import matplotlib.pyplot as plt
# 
# fig = plt.figure()
# plot = fig.add_subplot(111)
# 
# # create some curves
# for i in range(4):
#     plot.plot(i,i,'bo',gid=3)
# 
# plot.plot([0,1],[0,1],'r',gid=1)
# print (list(plot.get_lines()))
# 
# ann = None
# def on_plot_hover(event):
#     global ann
#     for point in plot.get_lines():
#         if point.contains(event)[0]:
#             ann = plot.annotate(point.get_gid(),xy=(point.get_gid(),point.get_gid()), xytext=(point.get_gid(),point.get_gid()-0.5),arrowprops=dict(facecolor='black', shrink=0.05),horizontalalignment='left', verticalalignment='bottom') 
# 
#     
# 
#             
# fig.canvas.mpl_connect('button_press_event', on_plot_hover)        
# plt.show()
#==============================================================================
#==============================================================================
# from matplotlib.pyplot import figure, show
# import numpy as npy
# from numpy.random import rand
# 
# 
# if 1: # picking on a scatter plot (matplotlib.collections.RegularPolyCollection)
# 
#     x, y, c, s = rand(4, 100)
#     print (x,y,c,s)
#     def onpick3(event):
#         ind = event.ind
#         print ('onpick3 scatter:', ind, npy.take(x, ind), npy.take(y, ind))
# 
#     fig = figure()
#     ax1 = fig.add_subplot(111)
#     col = ax1.scatter(x, y, 100*s, c, picker=True)
#     #fig.savefig('pscoll.eps')
#     fig.canvas.mpl_connect('pick_event', onpick3)
# 
# show()
#==============================================================================
