# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 18:45:01 2017

@author: kevin_000
"""
# (a : b) − (b : c) counts as 1

longestPathDict = {'a':'b','b':'c','c':'d','1':'2','2':'3','3':'4','4':'5', 5:3}
pathList = [];
           
def longestpath(d):
    # error checking
    if (len(d) == 0):
        print (maxPath(pathList))
        return;
    
    # set counter to 0
    counter = 0;
    
    # start on first key
    startKey = list(d)[0]
    nextKey = d.get(startKey) 
    del d[startKey]
    
    # find length of path
    while (d.get(nextKey) != None):
        startKey = nextKey;
        nextKey = d.get(nextKey)
        del d[startKey]
        counter += 1
        
    # add path to list
    pathList.append(counter)
    return longestpath(d)


def maxPath(l):
    maxValue = l[0]
    for i in l[1:]:
        if i > maxValue:
            maxValue = i
    return maxValue


# RUN THE FUNCTION # 
longestpath(longestPathDict)
# Output: 3