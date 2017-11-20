# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 18:45:15 2017

@author: kevin_000
"""
#==============================================================================
# P(win) = sigma(n=1,infiniti): P(win|Z=n)P(Z=n) = sigma(n=1,infiniti): (1/4)^n = 1/3
# P(win|Z=n) = 1/3
# P(Z=n) is a geometric random variable where the nth trial is the first success
# P(Z=n) = ((1/4)^n-1)*(3/4) 
#==============================================================================

import random
import time

random.seed(time.time())

def flip1in3():
    # 0 is tails 1 is heads
    # P(Z=n) is the chance I roll HH,HT,TH on the nth try
    # P(win|Z=n) is the chance I roll HH
    win = False
    while (not win):
        firstCoin = random.randint(0,1)
        secondCoin = random.randint(0,1)
        if (firstCoin != 0 or secondCoin != 0):
            if (firstCoin == 1 and secondCoin == 1):
                win = True;
            else:
                print ("YOU LOSE")
                return
            
    print ("YOU WIN")
    return


# RUN THE FUNCTION #
flip1in3()