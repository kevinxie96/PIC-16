# -*- coding: utf-8 -*-
"""
Created on Tue Apr 04 11:55:03 2017

@author: kevinxie96
"""
# input data ranges between 1000 A.D. and 5000 A.D. 

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
    if D < 1 or D > 31:
        print ("Please enter a Day integer between 1 and 31 inclusive")
        
    yearArray = list(str(Y))
    
    #apply leap year offset
    leapOffset = 0
    leapYear = False
    if ((Y%100 - Y%10) % 2) == 0:   # if decade is even
        leapOffset = evenDecadeOffset[yearArray[3]]
        if (Y%10) == 0 or (Y%10) == 4 or (Y%10) == 8:
            leapYear = True
    else:   # if decade is odd
        leapOffset = oddDecadeOffset[yearArray[3]]
        if (Y%10) == 2 or (Y%10) == 6:
            leapYear = True

    # apply century offset 
    decade = decadeChart.get(str(Y-Y%10));   # make ones digit 0
    centuryOffset = 0;
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
    
    # special expcetion for century leap years 
    if (int(yearArray[2]) == 0 and int(yearArray[3]) == 0) and (Y%400 != 0):
        leapYear = False
    # Jan and Feb offset       
    janAndFebOffset = 0
    if leapYear and M == 1 or M == 2:
        janAndFebOffset = -1
    # Calculate Day
    dayOfWeek = (D + monthChart[str(M)] + decade + centuryOffset + Y%10 + leapOffset + janAndFebOffset)%7   # algorithm 
    if dayOfWeek == 0:
        print ("Sunday")
    elif dayOfWeek == 1:
        print ("Monday")
    elif dayOfWeek == 2:
        print ("Tuesday")
    elif dayOfWeek == 3:
        print ("Wednesday")
    elif dayOfWeek == 4:
        print ("Thursday")
    elif dayOfWeek == 5:
        print ("Friday")
    else:
        print ("Saturday")
    return


# RUN THE FUNCTION # 
M = 1
D = 4
Y = 5000
weekday(M,D,Y)
# Output: Saturday

Y = 1000
weekday(M,D,Y)
# Output: Saturday