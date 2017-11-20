# -*- coding: utf-8 -*-
"""
Created on Wed May 10 12:09:02 2017

@author: kevinxie96
"""

# Challenge 1
#%%
"""
all_satisfiable(s) works like sympy’s satisfiable, but returns all possible satisfying assignments.
"""
import sympy as sp
import itertools
from sympy.logic.inference import satisfiable

def all_satisfiable(s):
    listOfSatisfiables = []
    listOfAtoms = list(s.atoms())
    numberOfSymbolicVariables = len(listOfAtoms)
    permutations = list(itertools.product ([False, True], repeat = numberOfSymbolicVariables))
    for i in permutations:
        potentialAnswer = dict([(listOfAtoms[x],i[x]) for x in range(numberOfSymbolicVariables)])
        if s.subs(potentialAnswer):
            listOfSatisfiables.append(potentialAnswer)
    return listOfSatisfiables

x,y,z=sp.symbols('x y z')
s1=(x|y)&(~x|~y)&(x|~y)&(~x|y)
s2=(x|y|z)&(~x|~y|~z)
print (all_satisfiable(s1))
print (all_satisfiable(s2))

# Challenge 2
#%%
"""
normalcurve(a,b) uses integration in sympy to write a function that takes as input two boundaries a,b, and returns the
probability that the a standard normal random variable falls in the interval between a and b.
"""
from sympy import oo

def normalcurve(a,b,mean=0,s_d=1):
    x=sp.symbols('x')
    normalRandomVariable = (1/(s_d*sp.sqrt(2*sp.pi)))*sp.exp(-((x-mean)**2)/2*(s_d**2))
    totalIntegral = sp.integrate(normalRandomVariable,(x,a,b))
    return totalIntegral.evalf()

a1,b1=[-1,1]
a2,b2=[0,oo]

print (normalcurve(a1,b1))
print (normalcurve(a2,b2))

# Challenge 3
#%%
"""
ball(v0) takes as input
the starting velocity, and outputs the point on the x-axis that the ball lands on, after it is thrown from the origin.
"""


def ball(v0):
    startingXvelocity = v0[0]
    startingYvelocity = v0[1]
    v,a,t = sp.symbols('v a t')
    d=v*t+.5*a*t**2
    timeSpentAscending = startingYvelocity/9.8
    highestHeight = d.subs({v:startingYvelocity,a:-9.8,t:timeSpentAscending})
    timeSpentDescending = sp.sqrt(highestHeight*2/9.8)
    return startingXvelocity*(timeSpentAscending+timeSpentDescending)

v0=[0,1]
w0=[1,0]
u0=[1,1]

print (ball(v0))
print (ball(w0))
print (ball(u0))

# Challenge 4
#%%
"""
balance(eq) balances chemical equations. So, it turns strings of the form ‘H2+O2=H2O’ into ‘2H2+O2=2H2O’.

"""
import numpy as np
np.set_printoptions(threshold=np.inf)
import copy
import re
from sympy.parsing.sympy_parser import parse_expr
from sympy import nsimplify

def balance(eq):
    #translate matrix
    chemEq = eq.replace(" ","")
    chemEq1 = chemEq.replace("=","+")
    whichVariable = chemEq1.split("+")
    
    chemEq = chemEq.split("=")
    
    chemEqLeft = chemEq[0]
    chemEqRight = chemEq[1]
    offset = 0
    whichVariableBefore = []
    whichVariableAfter = []
    for i in range(len(whichVariable)):
        if whichVariable[i] not in chemEqLeft:
            whichVariableBefore = whichVariable[0:i]
            whichVariableAfter = whichVariable[i:]
            offset = i
            break
    
    numbersAndElementsL = re.findall(r'[A-Z][a-z2-9]*', chemEqLeft)
    dicL = dict([(re.search(r'[A-Za-z]+',i).group(), int(re.search(r'[2-9]',i).group()) if re.search(r'[2-9]',i) else 1) for i in numbersAndElementsL])
    matrixOfInterest=[[0]*(len(whichVariable)+1)]*len(dicL)
    matrixOfInterest = np.array(matrixOfInterest)
    counterI = 0
    # before equal sign
    for i in dicL:
        for j in range(len(whichVariableBefore)):
            if i in whichVariableBefore[j]:
                index = whichVariableBefore[j].index(i)+len(i)
                if index >= len(whichVariableBefore[j]):
                    matrixOfInterest[counterI][j] = 1
                else:
                    value = whichVariableBefore[j][whichVariableBefore[j].index(i)+len(i)]  
                    matrixOfInterest[counterI][j] = int(value) if value.isdigit() else 1
                    if whichVariableBefore[j].count(i) > 1:
                        matrixOfInterest[counterI][j] = whichVariableBefore[j].count(i)
        counterI += 1
    # after equal sign
    counterI = 0
    for i in dicL:
        for j in range(len(whichVariableAfter)):
            if i in whichVariableAfter[j]:
                index = whichVariableAfter[j].index(i)+len(i)
                if index >= len(whichVariableAfter[j]):
                    matrixOfInterest[counterI][j+offset] = -1
                    matrixOfInterest[counterI][j+offset+1] = 0
                else:
                    value = whichVariableAfter[j][index]
                    matrixOfInterest[counterI][j+offset] = -int(value) if value.isdigit() else -1
                    if whichVariableAfter[j].count(i) > 1:
                        matrixOfInterest[counterI][j+offset] = -whichVariableAfter[j].count(i)
        
        counterI += 1
        
    # get solution
    matrixOfInterest = sp.Matrix(matrixOfInterest)
    n = len(whichVariable)
    x=[parse_expr('x%d'%i) for i in range(n)]
    x=sp.symbols('x0:%d'%n)
    sols=sp.solve_linear_system(matrixOfInterest,*x)
    valueDic = dict([(i,1) for i in x])
    for i in sols:
        valueDic[i] = nsimplify(sols[i].subs(valueDic))
    denominatorLCM = sp.lcm([sp.fraction(i)[1] for i in valueDic.values()])
    for i in valueDic:
        valueDic[i] = valueDic[i]*denominatorLCM
    
    counter1 = 0
    counter2 = 0
    returnString = ""
    for i in valueDic:
        if counter1 < len(whichVariableBefore):
            returnString += (str(valueDic[i]) if valueDic[i] > 1 else "")+whichVariableBefore[counter1] + (" + " if counter1 < (len(whichVariableBefore) - 1) else " = ")
        else:
            returnString += (str(valueDic[i]) if valueDic[i] > 1 else "")+whichVariableAfter[counter2] + (" + " if counter2 < (len(whichVariableAfter) - 1) else "")
            counter2 += 1
        counter1 +=1
    return returnString

eq = 'C6H6 + O2 = CO2 + H2O'
eq1 = 'AlI3 + HgCl2 = AlCl3 + HgI2'
print (balance(eq))
print (balance(eq1))
