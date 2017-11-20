# -*- coding: utf-8 -*-
from matplotlib.backends.backend_pdf import PdfPages
# Challenge 1
#%%
"""
fractal(var) designs and draws a fractal it with turtle, by writing a recursive function.
"""
import turtle as t

def fractal(n,L):
    if n==0:
        t.fd(L)
    else:
        fractal(n-1,L/3)
        t.right(90)
        fractal(n-1,L/3)
        t.left(90)
        fractal(n-1,L/3)
        t.left(90)
        fractal(n-1,L/3)
        t.right(90)
        fractal(n-1,L/3)
    return

#==============================================================================
# t.penup()
# t.setpos(-800,400)
# t.pendown()
# fractal(6,1500)
# s=t.getscreen()
# s.getcanvas().postscript(file = "fractal_304402775.eps")
# t.done()
#==============================================================================

# Challenge 2
#%%
"""
polygonT(n,sideLength) uses turtle and polygonP(n,sideLength,title) uses pyplot to 
draw regular n-gons with an optional length argument sideLength.
"""
import matplotlib.pyplot as plt
import numpy as np

def polygonT(n,sideLength=30):
    myangle = 360 / n
    for i in range(n):
        t.fd(sideLength)
        t.right(myangle)
        
#==============================================================================
# polygonT(8,60)
# s=t.getscreen()
# s.getcanvas().postscript(file = "octs_304402775.eps")
# t.done()
#==============================================================================

def polygonP(n,title,sideLength=3):
    fig = plt.figure()
    graph = fig.add_subplot(111)
    x=[sideLength * np.cos(2*np.pi*i/n) for i in range(n)]
    y=[sideLength * np.sin(2*np.pi*i/n) for i in range(n)]
    firstX = sideLength   #sideLength * math.cos(2*math.pi*0/n)   
    firstY = 0   #sideLength * math.sin(2*math.pi*0/n)
    x.append(firstX)
    y.append(firstY)
    graph.plot(x,y)
    graph.set_title(title)
    return fig


# Challenge 3
#%%
"""
scatter(filename,columntitle1,columntitle2,xlabel,ylabel) and histogram(filename,columntitle1,columntitle2,xlabel,ylabel) 
deploys matplotlibs to create two well-labeled, interesting data plots. One scatter plot, and one histogram.
"""
import pandas as pd

def scatter(filename,columntitle1,columntitle2,xlabel,ylabel,title):
    fig = plt.figure()
    graph = fig.add_subplot(111)
    lsd=pd.read_table(filename,'\s+')
    graph.plot(lsd[columntitle1],lsd[columntitle2],'ro')
    graph.axis([0, 350, 0, 4])
    graph.set_ylabel(xlabel)
    graph.set_xlabel(ylabel)
    graph.set_title(title)
    return fig

#specific function for the data set
def histogram(filename,column1,column2,column3,ylabel,title):
    histogramData=pd.read_table(filename,'\s+')
    fig = plt.figure()
    graph = fig.add_subplot(111)
    barwidth=.3
    graph.set_ylabel(ylabel)
    graph.set_title(title)
    graph.set_xticks(np.arange(4)+1/4)
    graph.set_xticklabels(['14-24','25-34','35-49','50-60'])
    graph.bar(np.arange(4),[histogramData[column3][0],histogramData[column3][3],histogramData[column3][6],histogramData[column3][9]],barwidth,color='r',label='Short Hair')
    graph.bar(np.arange(4)+barwidth,[histogramData[column3][1],histogramData[column3][4],histogramData[column3][7],histogramData[column3][10]],barwidth,color='g',label='Medium Hair')
    graph.bar(np.arange(4)+2*barwidth,[histogramData[column3][2],histogramData[column3][5],histogramData[column3][8],histogramData[column3][11]],barwidth,color='b',label='Long Hair')
    graph.legend()
    return fig

# Challenge 4
#%%
"""
a small network of your own choosing in a helpful way. This means that you may use
labels, directed edges, colors, etc..., if they are appropriate to help interpret the data. Find a network
that has some more information than just nodes and edges and visualize this (for example, directed
edges, different types of noed/edges, nodes belonging to different groups, etc...)

"""
Zachary_network=[[1,1,1,1,1,1,0,1,1],
[1,1,0,0,0,0,0,1,0],
[1,0,1,1,0,0,0,1,1],
[1,0,1,1,0,0,0,1,0],
[1,0,0,0,1,0,1,0,0],
[1,0,0,0,0,1,1,0,0],
[0,0,0,0,1,1,1,0,0],
[1,1,1,1,0,0,0,1,0],
[1,0,1,0,0,0,0,0,1]]

names = ['Linda','Kevin','Mason','Charlie','Jason','Albert','Daniel','Linh','Max']
gender = [0,1,1,1,1,1,1,0,1]   #0=female,1=male
colors = ['b','g','r','c','m','y','k','#ff9600','#C8C8C8']
def network_plot_circle(N,title):
    fig = plt.figure()
    graph = fig.add_subplot(111)
    n=len(N)
    x=[np.cos(2*np.pi*i/n) for i in range(n)]
    y=[np.sin(2*np.pi*i/n) for i in range(n)]
    graph.axis([-1.3, 1.3, -1.3, 1.3])
    for i in range(n):
        for j in range(i):
            if N[i][j]==1:
                graph.plot([x[i],x[j]],[y[i],y[j]],colors[i])   #the colors are random
    for i in range(n):
        color = ''
        if gender[i]==0:
            color = '#ff69b4'
            graph.plot(x[i],y[i],color='#ff69b4',marker='o')   #pink o for females
        else:
            color = 'blue'
            graph.plot(x[i],y[i],'bs')   #blue square for males
        graph.annotate(names[i], xy=(x[i],y[i]), xytext=(x[i],y[i]+0.2),arrowprops=dict(facecolor=color, shrink=0.05))
    graph.set_title(title)
    return fig

# Challenge 5
#%%
"""
def happinessArc(text,size) uses the Dodds et al happiness dictionary to create a happiness arc.
The size argument is how big of an interval we want.

"""
import re
from happiness_dictionary import happiness_dictionary as hd

def happinessArc(text, size, title):
    fig = plt.figure()
    graph = fig.add_subplot(111)
    listOfWords = re.findall(r'\w+',text.lower())
    x=[]
    y=[]
    for i in range(len(listOfWords)-size+1):
        rateTheText=""
        for j in range(size):
            rateTheText += listOfWords[i+j] + ','
        x.append(i+1)
        y.append(happiness(rateTheText))                         
    graph.set_ylabel('Score')
    graph.set_xticks([5,27,50])
    graph.set_xticklabels(['Beginning','Middle','End'])
    graph.set_title("Happiness Arc of " + title)
    graph.plot(x,y,'b')
    graph.plot(x,y,'bo')
    return fig
        
def happiness(textList):
    counter = 0;
    listOfWords = textList.split(",")[:len(textList)-1]
    for i in listOfWords:
        if i in hd:
            counter += hd[i]
            
    return counter

with PdfPages('pyplots_304402775.pdf') as pdf:
    pdf.savefig(polygonP(8,'Octagon'))
    pdf.savefig(scatter('tombstone.txt','SO2','Tombstone', 'Modelled 100-Year Mean SO2 Concentration','Marble Tombstone Mean Surface Recession Rate','Marble Tombstone Weathering and Air Pollution in North America'))
    pdf.savefig(histogram('hairlength.txt', 'HL','Age','Count','Count', 'An Approximation of Hair Length in the United states of America'))
    pdf.savefig(network_plot_circle(Zachary_network,"My Social Network"))
    pdf.savefig(happinessArc("Hear the sledges with the bells-- Silver bells!What a world of merriment their melody foretells! How they tinkle, tinkle, tinkle, In the icy air of night! While the stars that oversprinkle All the heavens, seem to twinkle With a crystalline delight; Keeping time, time, time, In a sort of Runic rhyme,To the tintinnabulation that so musically wells From the bells, bells, bells, bells, Bells, bells, bells-- From the jingling and the tinkling of the bells.",20, "'The Bells' Verse I"))