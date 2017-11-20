# -*- coding: utf-8 -*-
"""
Created on Mon Apr 03 12:37:39 2017

@author: kevinxie96
"""
# include 0 as a natural number

import math

def squaresupto(n):
    if n < 1:
        return
    else:
#==============================================================================
#         i in range(n+1):
#             sq = math.sqrt(i);
#             if sq == math.trunc(sq):
#                 print (i)
#==============================================================================
        print ([i for i in range(n+1) if math.sqrt(i) == math.trunc(math.sqrt(i))])   # list comprehension way
    return


# RUN THE FUNCTION #
squaresupto(16)
# Output: [0, 1, 4, 9, 16]