# -*- coding: utf-8 -*-
"""
Created on Sun May 14 19:18:23 2017

@author: kevin_000
"""
import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt

def darkhalf(im,p):
    n,m=im.shape
    im[0:int(n/2),:]*=p
    return im

im1=mpimg.imread('grayscale.png')
#==============================================================================
# print (im1)
# plt.imshow(im1, cmap = plt.get_cmap('gray'))
#==============================================================================
plt.imshow(darkhalf(im1,.5),cmap = plt.get_cmap('gray'))