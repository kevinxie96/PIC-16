# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 17:11:11 2017

@author: kevin_000
"""

# Challenge 1
#%%
"""
largerindex(l) is a function which takes as input a list l of numbers, and 
outputs a new list k, such that k[i] = 1 if l[i] > i, k[i] = 0 if l[i] = i, 
and k[i] = −1 if l[i] < i.

Input: the 1st input argument "l" is a list of numbers

Output: a printed list with values ranging from -1 to 1 inclusive

Challenge 1:
    Input >>> l=[1,2,0,4]
              largerindex(l)
    Output >>> [1, 1, -1, 1]
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
    return k

l=[1,2,0,4]
largerindex(l)

# Challenge 2
#%%
"""
squaresupto(n) is a function which takes as input a natural number n, and 
outputs a list of all the square numbers up to (and possibly including) n.

Input: the 1st input argument "n" is a number greater than or equal to 0

Output: a printed list of all the perfect square numbers

Challenge 2:
    Input >>> squaresupto(81)
    Output >>> [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
"""

import math

def squaresupto(n):
    if n < 1:
        return
    else:
# standard way
#==============================================================================
#         i in range(n+1):
#             sq = math.sqrt(i);
#             if sq == math.trunc(sq):
#                 print (i)
#==============================================================================
# list comprehension way
        outputList = [i for i in range(n+1) if math.sqrt(i) == math.trunc(math.sqrt(i))]
        print (outputList)
        return outputList

squaresupto(81)

# Challenge 3
#%%
"""
weekday(M,D,Y) is a function which the outputs the day of the week on date M/D/Y
It uses an algorithm similar to the one described on:
    https://en.wikipedia.org/wiki/Determination_of_the_day_of_the_week

Input: the 1st input argument M is a month integer (1<=M<=12), the 2nd input argument D 
is a day integer (1<=D<=31), and the 3rd input argument Y is an A.D. year integer 
(1000<=Y<=9999).

Output: a printed string which tells the user the day of the week

Challenge 3:
    Input >>> weekday(5,4,1987)
    Output >>> Monday
"""

monthChart = {'1':6,'2':2,'3':2,'4':5,'5':0,'6':3,'7':5,'8':1,'9':4,'10':6,'11':2,'12':4}   # 1 = January, 2 = February, ... etc
decadeChart = {'1900':1,'1910':6,'1920':5,'1930':3,'1940':2,'1950':0,'1960':6,'1970':4,'1980':3,'1990':1}
evenDecadeOffset = {'0':0,'1':0,'2':0,'3':0,'4':1,'5':1,'6':1,'7':1,'8':2,'9':2}
oddDecadeOffset = {'0':0,'1':0,'2':1,'3':1,'4':1,'5':1,'6':2,'7':2,'8':2,'9':2}

def weekday(M,D,Y):
    # error checking
    if not isinstance(M, int) or not isinstance(D, int) or not isinstance(Y, int):
        print ("Please enter integers for all input arguments")
        return
    if M < 1 or M > 12:
        print ("Please enter a Month integer between 1 and 12 inclusive")
        return
    if D < 1 or D > 31:
        print ("Please enter a Day integer between 1 and 31 inclusive")
        return
    if Y < 1000 or Y > 9999:
        print ("Please enter a Year integer between 1000 and 9999 inclusive")
        return
        
    yearArray = list(str(Y))   # break the year integer into a list
    
    # apply leap year offset
    leapOffset = 0   # leap year offset is 0 by default
    leapYear = False   # leap year is false by default
    if ((Y%100 - Y%10) % 2) == 0:   # if decade is even
        leapOffset = evenDecadeOffset[yearArray[3]]
        if (Y%10) == 0 or (Y%10) == 4 or (Y%10) == 8:
            leapYear = True   # then leap year is true
    else:   # if decade is odd
        leapOffset = oddDecadeOffset[yearArray[3]]
        if (Y%10) == 2 or (Y%10) == 6:
            leapYear = True   # then leap year is true

    # apply century offset 
    decade = decadeChart.get(str(Y-Y%10));   # make ones digit 0
    centuryOffset = 0;   # century offset is 0 by default
    if decade == None:
        decade = decadeChart["19" + yearArray[2] + "0"];       
        toCalculateOffset = yearArray[0] + yearArray[1]
        centuryDifference = (int(toCalculateOffset) - 19) % 4
        if centuryDifference == 1:
            centuryOffset = -1;
        elif centuryDifference == 2:
            centuryOffset = 4;
        elif centuryDifference == 3:
            centuryOffset = 2;
        else:
            centuryOffset = 0;   # remains 0 
    
    # special expcetion for century leap years (i.e. every 4th century is a leap year)
    if (int(yearArray[2]) == 0 and int(yearArray[3]) == 0) and (Y%400 != 0):
        leapYear = False
        
    # Jan and Feb offset for leap years      
    janAndFebOffset = 0   # Jan and Feb offset for leap years is 0 by default
    if leapYear and M == 1 or M == 2:
        janAndFebOffset = -1
        
    # Calculate Day
    dayOfWeek = (D + monthChart[str(M)] + decade + centuryOffset + Y%10 + leapOffset + janAndFebOffset)%7   # algorithm 
    if dayOfWeek == 0:
        dayOfWeek = "Sunday"
    elif dayOfWeek == 1:
        dayOfWeek ="Monday"
    elif dayOfWeek == 2:
        dayOfWeek ="Tuesday"
    elif dayOfWeek == 3:
        dayOfWeek ="Wednesday"
    elif dayOfWeek == 4:
        dayOfWeek ="Thursday"
    elif dayOfWeek == 5:
        dayOfWeek ="Friday"
    else:
        dayOfWeek ="Saturday"
    print (dayOfWeek)
    return dayOfWeek


weekday(5,4,1987)

# Challenge 4
#%%
"""
longestpath(d) is a function which finds the length of a longest path in a dictionary. 
Note that (a : b) − (b : c) counts as one; it's essentially counting the bridges
between the dictionary entries.

maxPath(l) is a helper function which iterates through a list and finds the max value.     

Input: the 1st input argument d is a dictionary

Output: a printed integer which informs the user of the longest path

Challenge 4:
    Input >>> d1={1:2,2:3,4:3}
              d2={1:2,2:3,3:4}
              d3={1:2,2:1}
              longestpath(d1)
              longestpath(d2)
              longestpath(d3)
              
    Output >>> 1
               2
               1
"""

pathList = [];
           
def longestpath(d):
    # error checking
    if (len(d) == 0):
        longestP = maxPath(pathList)
        print (longestP)
        pathList.clear()
        return longestP;
    
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

d1={1:2,2:3,4:3}
d2={1:2,2:3,3:4}
d3={1:2,2:1}
longestpath(d1)
longestpath(d2)
longestpath(d3)

# Challenge 5
#%%
"""
flip1in3() is a function which simulates a game in which 2 fair coins are utilized 
to give the user a 1/3 chance of winning. The probability theory is described by:
P(win) = sigma(n=1,infiniti): P(win|Z=n)P(Z=n) = sigma(n=1,infiniti): (1/4)^n = 1/3
P(win|Z=n) = 1/3
P(Z=n) is a geometric random variable where the nth trial is the first success
P(Z=n) = ((1/4)^n-1)*(3/4)
P(Z=n) is the chance I get HH,HT,TH on the nth try. If I get TT I try again.
P(win|Z=n) is the chance I get HH. If I get either HT or TH I lose.

Input: none

Output: a string describing whether the user won or lost

Challenge 5:
    Input >>> print (sum([flip1in3() for _ in range(1000)])/1000)
    Output >>> 0.336
"""

import random
import time

random.seed(time.time())

def flip1in3():
    # 0 is tails 1 is heads
    win = False
    while (not win):
        firstCoin = random.randint(0,1)
        secondCoin = random.randint(0,1)
        if (firstCoin != 0 or secondCoin != 0):
            if (firstCoin == 1 and secondCoin == 1):
                win = True;
            else:
                print ("YOU LOSE")
                return 0
            
    print ("YOU WIN")
    return 1

print (sum([flip1in3() for _ in range(1000)])/1000)