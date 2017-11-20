# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 12:14:37 2017

@author: kevinxie96
"""

import turtle as t

def koch_square(n,L):
    if n==0:
        t.fd(L)
    else:
        koch_square(n-1,L/3)
        t.left(90)
        koch_square(n-1,L/3)
        t.right(90)
        koch_square(n-1,L/3)
        t.right(90)
        koch_square(n-1,L/3)
        t.left(90)
        koch_square(n-1,L/3)
    return

#koch_square(5,800)

#t.done()

import matplotlib
import matplotlib.pyplot as plt

plt.plot(0,0,'o')
plt.plot((0,1),(2,3))

plt.axis([0,3,0,9])

plt.title('titlea')
plt.xlabel('aaa')
plt.ylabel('ssss')