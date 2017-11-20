# -*- coding: utf-8 -*-
"""
Created on Wed May 17 10:10:00 2017

@author: kevinxie96
"""
import copy

# Challenge 1
#%%
"""
These four types of sorting algorithms take a list of
real numbers as input, and output a list with the same set of numbers, but ordered from low to high.
"""
def select_sort(n):
    d = copy.copy(n)
    for i in range(len(n)):
        minI = i
        for j in range(len(n))[i+1:]:
            if d[minI] > d[j]:
                minI = j
        temp = d[i]
        d[i] = d[minI]
        d[minI] = temp
    return d
    
def bubble_sort(n):
    d = copy.copy(n)
    counter = 0
    while (counter < len(n)-1):
        for i in range(len(n))[0:len(n)-counter-1]:
            if d[i] > d[i+1]:
                temp = d[i]
                d[i] = d[i+1]
                d[i+1] = temp
        counter += 1
    return d

def merge_sort(n):
    if len(n) <= 1:
        return n
    middle = int (len(n)/2)
    left = n[:middle]
    right = n[middle:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left,right)

def merge(left,right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i+=1
    while j < len(right):
        result.append(right[j])
        j+=1
    return result

def quick_sort(n,lo,hi):
    if lo<hi:
        p = partition(n,lo,hi)
        quick_sort(n,lo,p-1)
        quick_sort(n,p+1,hi)
    return n
    
def partition(n,lo,hi):
    pivot = n[hi]
    i = lo-1
    for j in range(lo,hi):
        if n[j] <= pivot:
            i += 1
            temp = n[i]
            n[i] = n[j]
            n[j] = temp
    temp = n[i+1]
    n[i+1] = n[hi]
    n[hi] = temp
    return i+1

d=[3, 2, 5, 2, 4]
print (select_sort(d))
print (bubble_sort(d))
print (merge_sort(d))
print (quick_sort(d,0,len(d)-1))

# Challenge 2
#%%
"""
There are lists of natural numbers 1, . . . , n in randomized order.
The function graph_algorthms(n) measures the time it takes to sort them for different
values of n. Plots your results in one well-labeled figure.
"""
import random as ran
from timeit import default_timer as timer
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

def graph_algorithms(n):
    randomSuperList= [ran.getrandbits(10) for r in range(n)]
    listOLists = []
    for i in range(n):
        listOLists.append(randomSuperList[0:i+1])

    fig = plt.figure()
    graph = fig.add_subplot(111)
    x = range(len(listOLists))
    ySelec = []
    yBubb = []
    yMerg = []
    yQuic = []
    for i in listOLists:
        start = timer()
        select_sort(i)
        end = timer()
        ySelec.append(end-start)
    for i in listOLists:
        start = timer()
        bubble_sort(i)
        end = timer()
        yBubb.append(end-start)
    for i in listOLists:
        start = timer()
        merge_sort(i)
        end = timer()
        yMerg.append(end-start)
    for i in listOLists:
        start = timer()
        quick_sort(i,0,len(i)-1)
        end = timer()
        yQuic.append(end-start)
    graph.set_title('Sorting Algorithm Comparison')
    graph.set_ylabel('Seconds')
    graph.set_xlabel('List Length (n)')
    graph.plot(x,ySelec,'b', label='Selection Sort')
    graph.plot(x,yBubb,'r', label='Bubble Sort')
    graph.plot(x,yMerg,'m', label='Merge Sort')
    graph.plot(x,yQuic,'k', label='Quick Sort')
    graph.legend()
    return fig
#==============================================================================
#     graph.set_title("Algorithm Comparisons")
#     graph.plot(x,y,'b')
#     graph.plot(x,y,'bo')
#     return fig
#==============================================================================
graph_algorithms(200)
#==============================================================================
# with PdfPages('hw7_304402775.pdf') as pdf:
#     pdf.savefig(graph_algorithms(500))
#==============================================================================
# Challenge 3
#%%
"""
Given a (weighted, directed) network as an n × n array, and two nodes v and w, write an algorithm
(implementation of Dijkstra) that finds a shortest path from startnode to endnode.
"""
import numpy as np

N=np.array([[0,2,1,0],[2,0,1,2],[1,1,0,1],[0,1,2,0]])

def dijkstra_shortestpath(N,startnode,endnode):
    maxV = np.sum(N)*2
    n = len(N)
    cost = [[maxV if N[i][j] == 0 else N[i][j] for j in range(n)] for i in range(n)]
    shortDist = []
    prev = []
    visited = []
    nextnode = 0
    
    for i in range(n):
        shortDist.append(cost[startnode][i])
        prev.append(startnode)
        visited.append(0)
        
    shortDist[startnode] = 0
    visited[startnode] = 1
    count = 1
    
    while (count <n-1):
        minDist = maxV
        for i in range(n):
            if shortDist[i] < minDist and not visited[i]:
                minDist = shortDist[i]
                nextnode = i
        visited[nextnode] = 1
        for i in range(n):
            if not visited[i]:
                if minDist+cost[nextnode][i]<shortDist[i]:
                    shortDist[i]=minDist+cost[nextnode][i]
                    prev[i] = nextnode
                    
        count+=1
    outputString = ""
    if shortDist[endnode] != maxV:
        j=prev[endnode]
        output = [endnode,prev[endnode]]
        while(j != startnode):
            j=prev[j]
            output.append(j)
        for i in output[::-1]:
            outputString += str(i) + ("->" if i != endnode else "")
    return (shortDist[endnode],outputString)
        
    
print (dijkstra_shortestpath(N,0,3))
            
# Challenge 4
#%%
import sympy as sp
from sympy.logic.inference import satisfiable
x,y,z=sp.symbols('x y z')
s1=(x|y)&(~x|~z)&(~y|x)&(y|z)&(~z|y)
s2=(x|z)&(~x|z)&(y|~z)&(~y|~z)



def two_sat(s1):
    # create dictionary keys
    listOfAtoms = list(s1.atoms())
    negationList = [~x for x in listOfAtoms]
    listOfAtoms.extend(negationList)
    networkDict = dict([(x,[]) for x in listOfAtoms])

    # bind keys to values
    for i in range(len(s1.args)):
        networkDict[~s1.args[i].args[0]].append(s1.args[i].args[1])
        networkDict[~s1.args[i].args[1]].append(s1.args[i].args[0])
    
    unassignedVariables = listOfAtoms
    assignedVariables = {}
    while (len(unassignedVariables) != 0):
        x = unassignedVariables[len(unassignedVariables)-1]
        x_to_negation_x = BFS(networkDict,x)
        negation_x_to_x = BFS(networkDict,~x)
        x1 = ~x in x_to_negation_x
        x2 = x in negation_x_to_x
        if (x1 and x2):
            return False
        assignedVariables[~x] = True if x1 or (not x1 and not x2) else False
        assignedVariables[x] = True if x2 else False
        unassignedVariables.remove(~x)
        unassignedVariables.remove(x)
        if assignedVariables[~x]:
            for i in negation_x_to_x:
                if i in unassignedVariables:
                    assignedVariables[i] = True
                    assignedVariables[~i] = False
                    unassignedVariables.remove(i)
                    unassignedVariables.remove(~i)
        if assignedVariables[x]:
            for i in x_to_negation_x:
                if i in unassignedVariables:
                    assignedVariables[i] = True
                    assignedVariables[~i] = False
                    unassignedVariables.remove(i)
                    unassignedVariables.remove(~i)
    return assignedVariables
def BFS(N,x):
    Q=[x]
    V=[]
    while Q:
        for i in N[Q[0]]:
            if i not in V and i not in Q:
                Q.append(i)
        V.append(Q.pop(0))
    return V
print (two_sat(s1))
print (two_sat(s2))