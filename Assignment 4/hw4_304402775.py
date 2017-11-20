# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 13:17:52 2017

@author: kevin_000
"""
from matplotlib.backends.backend_pdf import PdfPages

# Challenge 1
#%%
"""
heart(im) takes an image as input, and outputs a heart-shaped cut-out of it on a pink
background. The shape of the heart will need to depend on the dimensions of the image, so that you
do not cut too much of the image.
"""
import matplotlib
import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt
matplotlib.rcParams.update({'font.size': 6})

def heart(im):
    img=mpimg.imread(im)
    width,height = img.shape
    x,y=np.ogrid[0:width, 0:height]
    mask=(x-width/3.5>y)
    img[mask] = [255,192,203]
    mask=(-x+width/3.5+width<y)
    img[mask] = [255,192,203]
    mask = (x<-(width/6)*np.sin(y*np.pi/(width/2)) + width/3.5)&(y<width/2)
    img[mask] = [255,192,203]
    mask = (x<-(width/6)*np.sin(y*np.pi/(width/2)-np.pi) + width/3.5)&(y>width/2)
    img[mask] = [255,192,203]
    return img


# Challenge 2
#%%
"""
blurring(im,method) takes a gray-scale picture, and offers two options for noise removal: uniform or
gaussian
"""
def salt_pepper(im,ps=.1,pp=.1):
    im1=mpimg.imread(im)
    n,m=im1.shape
    for i in range(n):
        for j in range(m):
            b=np.random.uniform()
            if b<ps:
                im1[i,j]=0
            elif b>1-pp:
                im1[i,j]=1
    noisy_im=[[[im1[i,j]]*3 for j in range(m)] for i in range(n)]
    return noisy_im

def blurring(im,method,k=5,sigma=7):
    img=mpimg.imread(im)
    img = np.array(img, dtype='float')
    if method != 'gaussian' and method !='uniform':
        print ("Please enter either gaussian or uniform")
        return
    if k%2==0:
        print ("Enter an odd k")
        return
    blurFilter = [[0]*k]*k
    im=[[0]*img.shape[1]]*img.shape[0]
    im=np.array(im,dtype='float')
    if method == 'uniform':
        blurFilter = [[1/k**2]*k]*k
        blurFilter = np.array(blurFilter,dtype='float')
        for i in range(img.shape[0])[int(k/2):img.shape[0]-int(k/2)]:
            for j in range(img.shape[1])[int(k/2):img.shape[1]-int(k/2)]:
                subImageSquare = img[int(i-(k-1)/2):int((i+(k-1)/2)+1),int(j-(k-1)/2):int((j+(k-1)/2)+1)]
                subImageSquare = np.array(subImageSquare,dtype='float')
                im[i][j] = np.sum(subImageSquare*blurFilter)
    else:
        for i in range(img.shape[0])[int(k/2):img.shape[0]-int(k/2)]:
            for j in range(img.shape[1])[int(k/2):img.shape[1]-int(k/2)]:
                subImageSquare = img[int(i-(k-1)/2):int((i+(k-1)/2)+1),int(j-(k-1)/2):int((j+(k-1)/2)+1)]
                subImageSquare = np.array(subImageSquare,dtype='float')
                blurFilter = [[(1/(2*np.pi*sigma**2))*np.exp(-(((i-(k-1)/2)**2)+((j-(k-1)/2)**2))/(2*sigma**2)) for j in range(int(j-(k-1)/2),int((j+(k-1)/2)+1))] for i in range(int(i-(k-1)/2),int((i+(k-1)/2)+1))]
                blurFilter = np.array(blurFilter,dtype='float')
                im[i][j] = np.sum(subImageSquare*blurFilter)/np.sum(blurFilter)
    return im


# Challenge 3
#%%
"""
detect_edge(im,method) takes a gray-scale image and detects edges, with the option of horizontal, vertical
or both.
"""
sobel_x = [[-1.0,0.0,1.0],
           [-2.0,0.0,2.0],
           [-1.0,0.0,1.0]]

sobel_y = [[-1.0,-2.0,-1.0],
           [0.0,0.0,0.0],
           [1.0,2.0,1.0]]

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])


def detect_edge(img,method):
    if method != 'horizontal' and method != 'vertical' and method != 'both':
        print ("Please enter for the second argument 'horizontal', 'vertical', or 'both'")
        return
    else:
        img=mpimg.imread(img)
        im=[[0]*img.shape[1]]*img.shape[0]
        im=np.array(im,dtype='float')
        for x in range(img.shape[0])[1:img.shape[0]-1]:
            for y in range(img.shape[1])[1:img.shape[1]-1]:
                val = 0
                pixel_x = 0
                pixel_y = 0
                if method == 'horizontal':
#==============================================================================
#                     pixel_x = (sobel_x[0][0] * img[x-1][y-1]) + (sobel_x[0][1] * img[x][y-1]) + (sobel_x[0][2] * img[x+1][y-1]) + (sobel_x[1][0] * img[x-1][y])   + (sobel_x[1][1] * img[x][y])   + (sobel_x[1][2] * img[x+1][y]) + (sobel_x[2][0] * img[x-1][y+1]) + (sobel_x[2][1] * img[x][y+1]) + (sobel_x[2][2] * img[x+1][y+1])
#==============================================================================
                    pixel_x = (sobel_x[0][0] * img[x-1][y-1]) + (sobel_x[0][1] * img[x-1][y]) + (sobel_x[0][2] * img[x-1][y+1]) + (sobel_x[1][0] * img[x][y-1])   + (sobel_x[1][1] * img[x][y])   + (sobel_x[1][2] * img[x][y+1]) + (sobel_x[2][0] * img[x+1][y-1]) + (sobel_x[2][1] * img[x+1][y]) + (sobel_x[2][2] * img[x+1][y+1])
                elif method == 'vertical':
#==============================================================================
#                     pixel_y = (sobel_y[0][0] * img[x-1][y-1]) + (sobel_y[0][1] * img[x][y-1]) + (sobel_y[0][2] * img[x+1][y-1]) + (sobel_y[1][0] * img[x-1][y])   + (sobel_y[1][1] * img[x][y])   + (sobel_y[1][2] * img[x+1][y]) + (sobel_y[2][0] * img[x-1][y+1]) + (sobel_y[2][1] * img[x][y+1]) + (sobel_y[2][2] * img[x+1][y+1])
#==============================================================================
                    pixel_y = (sobel_y[0][0] * img[x-1][y-1]) + (sobel_y[0][1] * img[x-1][y]) + (sobel_y[0][2] * img[x-1][y+1]) + (sobel_y[1][0] * img[x][y-1])   + (sobel_y[1][1] * img[x][y])   + (sobel_y[1][2] * img[x][y+1]) + (sobel_y[2][0] * img[x+1][y-1]) + (sobel_y[2][1] * img[x+1][y]) + (sobel_y[2][2] * img[x+1][y+1])
                else:
                    pixel_x = (sobel_x[0][0] * img[x-1][y-1]) + (sobel_x[0][1] * img[x-1][y]) + (sobel_x[0][2] * img[x-1][y+1]) + (sobel_x[1][0] * img[x][y-1])   + (sobel_x[1][1] * img[x][y])   + (sobel_x[1][2] * img[x][y+1]) + (sobel_x[2][0] * img[x+1][y-1]) + (sobel_x[2][1] * img[x+1][y]) + (sobel_x[2][2] * img[x+1][y+1])
                    pixel_y = (sobel_y[0][0] * img[x-1][y-1]) + (sobel_y[0][1] * img[x-1][y]) + (sobel_y[0][2] * img[x-1][y+1]) + (sobel_y[1][0] * img[x][y-1])   + (sobel_y[1][1] * img[x][y])   + (sobel_y[1][2] * img[x][y+1]) + (sobel_y[2][0] * img[x+1][y-1]) + (sobel_y[2][1] * img[x+1][y]) + (sobel_y[2][2] * img[x+1][y+1])
                val = np.sqrt((pixel_x * pixel_x) + (pixel_y * pixel_y))/np.sqrt(32)
                im[x][y] = val
        return im

#==============================================================================
# img=mpimg.imread('grayscale.png')
# plt.imshow(detect_edge(img,'both'),cmap = plt.get_cmap('gray'))
#==============================================================================

# Challenge 4
#%%
"""
otsu_threshold(im) splits a gray-scale image into foreground and background using Otsu’s thresholding
method.
"""

def histogramDataogram(img):
    width,height = img.shape
    histogramData = [0]*256
    
    for y in range(height):
        for x in range(width):
            gray_level= img[x,y]
            grayLevel255 = gray_level
            histogramData[int(grayLevel255)] = histogramData[int(grayLevel255)]+1
    return histogramData


def get_threshold(img):
    img=np.array(rgb2gray(mpimg.imread(img)),dtype='float')
    width,height = img.shape
    histogramData = histogramDataogram(img)
    sum_all = 0
    
    # sum of all pixel values in the picture
    for t in range(256):
        sum_all += t * histogramData[t]
        
    sum_back = 0
    numberOfBackgroundPixels = 0 # number of background pixels
    numberOfForegroundPixels = 0 # number of the foreground pixels
    var_max = 0 
    threshold = 0
    totalNumberOfPixels = height*width
    
    for t in range(256):
        numberOfBackgroundPixels += histogramData[t]
        if (numberOfBackgroundPixels == 0): continue
        numberOfForegroundPixels = totalNumberOfPixels - numberOfBackgroundPixels
        if (numberOfForegroundPixels == 0): break
        # calculate  means
        sum_back += t * histogramData[t]
        meanBackgroundValue = sum_back / numberOfBackgroundPixels 
        meanForegroundValue = (sum_all - sum_back) / numberOfForegroundPixels 
        # between class variance
        var_between = numberOfBackgroundPixels * numberOfForegroundPixels * (meanBackgroundValue - meanForegroundValue)**2 
        if (var_between > var_max):
            var_max = var_between
            threshold = t
    return threshold

def otsu_threshold(img, threshold=100):
    img=np.array(rgb2gray(mpimg.imread(img)),dtype='float')
    width,height = img.shape
    im=[[0]*img.shape[1]]*img.shape[0]
    im=np.array(im,dtype='float')
    for x in range(width):
        for y in range(height):
            if img[x,y] < threshold: # high gray levels in foreground
                im[x,y] = 1 # white foreground
            else: # low gray levels in background 
                im[x,y] = 0 # black background
    return im

#==============================================================================
# img=mpimg.imread('grayscale.png')
# plt.imshow(otsu_threshold(img, get_threshold(img)),cmap = plt.get_cmap('gray'))
#==============================================================================

# Challenge 5
#%%
"""
blur_background(im) combines your first and third challenge, by identifying the background of an
image, and blurring it.
"""
def blurring1(im,method,k=23,sigma=7):
    img=np.array(rgb2gray(mpimg.imread(im)),dtype='float')
    if method != 'gaussian' and method !='uniform':
        print ("Please enter either gaussian or uniform")
        return
    if k%2==0:
        print ("Enter an odd k")
        return
    blurFilter = [[0]*k]*k
    im=[[0]*img.shape[1]]*img.shape[0]
    im=np.array(im,dtype='float')
    if method == 'uniform':
        blurFilter = [[1/k**2]*k]*k
        blurFilter = np.array(blurFilter,dtype='float')
        for i in range(img.shape[0])[int(k/2):img.shape[0]-int(k/2)]:
            for j in range(img.shape[1])[int(k/2):img.shape[1]-int(k/2)]:
                subImageSquare = img[int(i-(k-1)/2):int((i+(k-1)/2)+1),int(j-(k-1)/2):int((j+(k-1)/2)+1)]
                subImageSquare = np.array(subImageSquare,dtype='float')
                im[i][j] = np.sum(subImageSquare*blurFilter)
    else:
        for i in range(img.shape[0])[int(k/2):img.shape[0]-int(k/2)]:
            for j in range(img.shape[1])[int(k/2):img.shape[1]-int(k/2)]:
                subImageSquare = img[int(i-(k-1)/2):int((i+(k-1)/2)+1),int(j-(k-1)/2):int((j+(k-1)/2)+1)]
                subImageSquare = np.array(subImageSquare,dtype='float')
                blurFilter = [[(1/(2*np.pi*sigma**2))*np.exp(-(((i-(k-1)/2)**2)+((j-(k-1)/2)**2))/(2*sigma**2)) for j in range(int(j-(k-1)/2),int((j+(k-1)/2)+1))] for i in range(int(i-(k-1)/2),int((i+(k-1)/2)+1))]
                blurFilter = np.array(blurFilter,dtype='float')
                im[i][j] = np.sum(subImageSquare*blurFilter)/np.sum(blurFilter)
    return im

def blur_background(img, threshold=100,method='uniform',k=7):
    img1=np.array(rgb2gray(mpimg.imread(img)),dtype='float')
    im1 = blurring1(img,method,k)
    width,height = img1.shape
    for x in range(width):
        for y in range(height):
            if img1[x,y] < threshold: # high gray levels in foreground
                im1[x,y] = img1[x,y]
    return im1

#==============================================================================
# img=mpimg.imread('grayscale.png')
# plt.imshow(blur_background(img,get_threshold(img)),cmap = plt.get_cmap('gray'))
#==============================================================================

#==============================================================================
# fig = plt.figure()
# graph = fig.add_subplot(111)
# graph.imshow(mpimg.imread('dog.jpg'))
# graph.set_title("Original Photo, 'dog.jpg', for Challenge 1 heart(im)")
# fig0 = plt.figure()
# graph = fig0.add_subplot(111)
# graph.imshow(heart('dog.jpg'))
# graph.set_title("After Photo for heart('dog.jpg')")
# fig1 = plt.figure()
# graph = fig1.add_subplot(111)
# graph.set_title("Original Photo, 'blurry.png', for Challenge 2 blurring(im,method)")
# graph.imshow(mpimg.imread('blurry.png'),cmap = plt.get_cmap('gray'))
# fig2 = plt.figure()
# graph = fig2.add_subplot(111)
# graph.set_title("After Photo for blurring('blurry.png','uniform',k=7)")
# graph.imshow(blurring('blurry.png','uniform',k=7), cmap = plt.get_cmap('gray'))
# fig3 = plt.figure()
# graph = fig3.add_subplot(111)
# graph.set_title("After Photo for blurring('blurry.png','gaussian',k=11,sigma=20)")
# graph.imshow(blurring('blurry.png','gaussian',11,20), cmap = plt.get_cmap('gray'))
# fig4 = plt.figure()
# graph = fig4.add_subplot(111)
# graph.set_title("Original Photo, 'grayscale.png', for Challenge 3 detect_edge(img,method)")
# graph.imshow(mpimg.imread('grayscale.png'), cmap = plt.get_cmap('gray'))
# fig5 = plt.figure()
# graph = fig5.add_subplot(111)
# graph.set_title("After Photo for detect_edge('grayscale.png','both')")
# graph.imshow(detect_edge('grayscale.png','both'),cmap = plt.get_cmap('gray'))
#==============================================================================
fig5a = plt.figure()
graph = fig5a.add_subplot(111)
graph.set_title("Original Photo, 'dikembe.jpg', for Challenge 4,5")
graph.imshow(rgb2gray(mpimg.imread('dikembe.jpg')),cmap = plt.get_cmap('gray'))
fig6 = plt.figure()
print (rgb2gray(mpimg.imread('dikembe.jpg')))
graph = fig6.add_subplot(111)
graph.set_title("After Photo for otsu_threshold('dikembe.jpg', get_threshold('dikembe.jpg'))")
graph.imshow(otsu_threshold('dikembe.jpg', get_threshold('dikembe.jpg')),cmap = plt.get_cmap('gray'))
fig7 = plt.figure()
graph = fig7.add_subplot(111)
graph.set_title("After Photo for blur_background('dikembe.jpg', get_threshold('dikembe.jpg')), method='uniform',k=7")
graph.imshow(blur_background('dikembe.jpg',get_threshold('dikembe.jpg')),cmap = plt.get_cmap('gray'))

#==============================================================================
# with PdfPages('pyplots_304402775_hw4.pdf') as pdf:
#     pdf.savefig(fig)
#     pdf.savefig(fig0)
#     pdf.savefig(fig1)
#     pdf.savefig(fig2)
#     pdf.savefig(fig3)
#     pdf.savefig(fig4)
#     pdf.savefig(fig5)
#     pdf.savefig(fig6)
#     pdf.savefig(fig7)
#==============================================================================
with PdfPages('pyplots_304402775.pdf') as pdf:
      pdf.savefig(fig5a)
      pdf.savefig(fig6)
      pdf.savefig(fig7)

