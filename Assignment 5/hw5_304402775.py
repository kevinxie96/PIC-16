# -*- coding: utf-8 -*-
"""
Created on Thu May  4 22:57:02 2017

@author: kevin_000
"""


# Challenge 1
#%%
"""
corrcoeff(x,y) takes two vectors of length n as input (representing two variables at n observations),
and outputs the correlation coefficient between them.

"""
import numpy as np
from numpy import linalg as LA

def corrcoeff(x,y):
    if len(x) != len(y):
        print("Vectors must be same length")
        return
    xMean = np.mean(x)
    yMean = np.mean(y)
    deviationX = [x[i]-xMean for i in range(len(x))]
    deviationY = [y[i]-yMean for i in range(len(y))]
    deviationX = np.array(deviationX,dtype='float')
    deviationY = np.array(deviationY,dtype='float')
    return np.dot(deviationX,deviationY)/(LA.norm(deviationX,2)*LA.norm(deviationY,2))

a=[1,6,2,9]
b=[8,2,7,1]
print (corrcoeff(a,b))
# Challenge 2
#%%
"""
degree_in(N) takes a (possibly weighted) network as input, and outputs two vectors, one of
which gives the in-degree of each node (the weight of all the edges pointing to the node), 
and one which ranks the nodes by degree/strength, highest to lowest.

degree_out(N) takes a (possibly weighted) network as input, and outputs two vectors, one of
which gives the out-degree of each node (the weight of all the edges pointing away from the node), 
and one which ranks the nodes bydegree/strength, highest to lowest.
"""
Zachary_network=[[1,1,1,1,1,1,1,1,1,0,1,1,1,1,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,0],
[1,1,1,1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,1,0,0,0],
[1,1,1,1,0,0,0,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0],
[1,1,1,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1],
[0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,1,1,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
[0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1],
[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,0,1,1],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,0,0,1,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,1,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,1],
[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0,0,1],
[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,1,1],
[0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,1,1,1],
[0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,1,0,0,1,0,1,0,1,1,0,0,0,0,0,1,1,1,1,1],
[0,0,0,0,0,0,0,0,1,1,0,0,0,1,1,1,0,0,1,1,1,0,1,1,0,0,1,1,1,1,1,1,1,1]]

def degree_out(N):
    transposedNetwork = np.transpose(N)
    degreeVector = [np.sum(i) for i in transposedNetwork]
    return np.array(degreeVector),np.sort(degreeVector)[::-1]

def degree_in(N):
    degreeVector = [np.sum(i) for i in N]
    return np.array(degreeVector),np.sort(degreeVector)[::-1]

print (degree_out(Zachary_network))
print (degree_in(Zachary_network))

# Challenge 3
#%%
"""
pagerank(N) uses linear algebra from numpy that takes a (possibly weighted, directed network)
as input, and outputs two vectors, one that gives the score for each node, and one vector that
ranks the nodes from highest pagerank score to lowest.
"""

import math
np.set_printoptions(threshold=np.inf)


def makeColumnsSumTo1(N):
    N = np.transpose(N)
    for i in range(len(N)):
        sum1 = np.sum(N[i])
        for j in range(len(N[i])):
            N[i][j] = N[i][j]/sum1
    return np.transpose(N)

print (makeColumnsSumTo1(np.array(Zachary_network,dtype='float')))
#==============================================================================
# w,v=LA.eig(np.diag((1, 2, 3)))
# print (w[0]==1.)
#==============================================================================
                  
def pagerank(N):
    n,v = LA.eig(N)
    nTF = np.iscomplex(n)
    nReal = n.real
    for i in range(len(n)):
        if math.ceil(nReal[i]) == 1 and nTF[i] == False:
            outputRanks = np.array([v[j][i] for j in range(len(N[0]))])
            normalize = np.sum(outputRanks)
            outputRanks = np.array([i/normalize for i in outputRanks])
            return outputRanks,np.sort(outputRanks)[::-1]

print (pagerank(makeColumnsSumTo1(np.array(Zachary_network,dtype='float'))))

# Challenge 4
#%%
"""
similarity(T) takes a set of tweets (given as a list of one string for each tweet), and outputs a
network where the edges represent the similarity between pairs of tweets, based on common words.
Think about different ways to compute this score. 

Details: The matrix should be read in a from row entry to height entry format. For example, [0,1] 
has a value of 1. which means all of the words in the first node exist in the second node. [1,0] 
has a value of 0.5 which means half of the words in the second node exist in the first node.


Areas of Improvement: I need to add weighted values for words following # and @ as they are the focus 
of a typical tweet.
"""
import re

L=['dog dog', 'dog cat', 'cat cat']
def similarity(T):
    listOfDictionariesForBasicWords = []
#==============================================================================
#     listOfDictionariesForHashTagWords = []
#     listOfDictionariesForUsers = []
#==============================================================================
    # form dictionaries for each tweet
    for tweet in T:
        words=re.findall(r'[\w\']+',tweet)
#==============================================================================
#         users = re.findall(r'@([\w\']+)',tweet)
#         tags = re.findall(r'#([\w\']+)',tweet)
#         words = [x for x in words if x not in users]   # remove users
#         words = [x for x in words if x not in tags]   # remove tags
#         dictTags = dict([(x,tags.count(x)) for x in tags])
#         dictUsers = dict([(x,users.count(x)) for x in users])
#==============================================================================
        
        dictWordsSum = len(words)
        dictWords = dict([(x,words.count(x)/dictWordsSum) for x in words])
        
#==============================================================================
#         dictTagsSum = 0
#         for x in dictTags.values():
#             dictTagsSum += x
#         dictTags = dict([(x,2*tags.count(x)/dictTagsSum) for x in tags])   # tags get x2 multiplier 
#         
#         dictUsersSum = 0
#         for x in dictUsers.values():
#             dictUsersSum += x
#         dictUsers = dict([(x,3*users.count(x)/dictUsersSum) for x in users])   # users get a x3 mutliplier 
#         
#==============================================================================
        listOfDictionariesForBasicWords.append(dictWords)
#==============================================================================
#         listOfDictionariesForHashTagWords.append(dictTags)
#         listOfDictionariesForUsers.append(dictUsers)
#==============================================================================
        
    outputNetwork = [[0]*len(L)]*len(L)
    outputNetwork = np.array(outputNetwork,dtype='float')
    for i in range(len(listOfDictionariesForBasicWords)):
        for j in range(len(listOfDictionariesForBasicWords))[i+1:]:
            itojScore = 0
            jtoiScore = 0
            for k in (listOfDictionariesForBasicWords[i].keys() & listOfDictionariesForBasicWords[j]):
                itojScore += listOfDictionariesForBasicWords[i][k]
                jtoiScore += listOfDictionariesForBasicWords[j][k]
            outputNetwork[i][j] = itojScore
            outputNetwork[j][i] = jtoiScore

    return outputNetwork

print (similarity(L))