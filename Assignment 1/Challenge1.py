# -*- coding: utf-8 -*-
"""
Created on Mon Apr 03 12:34:29 2017

@author: kevinxie96
"""
def largerindex(l):
    k = [];
    for i in range(len(l)):
        if l[i] > i:
            k.append(1)
        elif l[i] == i:
            k.append(0)
        else:
            k.append(-1)          
    print (k)
    return


# RUN THE FUNCTION #
l = [0,3,1,3,2,5,4,7]   # create list
largerindex(l)   # pass in list
# Output: [0, 1, -1, 0, -1, 0, -1, 0]