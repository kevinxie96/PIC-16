# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 00:30:59 2017

@author: kevin_000
"""

def powerlists(L,k):
    superList = [[j**i for j in L] for i in range(k+1) if (i!=0)]
    return superList
    
L = [2,5,1]
k=4
print (powerlists(L,k))