# -*- coding: utf-8 -*-
"""
SYS-611: Example Markov Process Generator

@author: Paul T. Grogan, pgrogan@stevens.edu
"""

# import the python3 behavior for importing, division, and printing in python2
from __future__ import absolute_import, division, print_function

# import the numpy package and refer to it as `np`
# see http://docs.scipy.org/doc/numpy/reference/ for documentation
import numpy as np
# import the matplotlib.pyplot package and refer to it as `plt`
import matplotlib.pyplot as plt

#5.1

def next_state(q):
    r = np.random.rand()
    if q == 4:
        #homerun
        return 0
    elif q == 0:
        #home plate
        if r <= 0.52:
            return 0
        elif r <= 0.933:
            #1st
            return 1
        elif r <= 0.977:
            #2nd
            return 2
        elif r <= 0.996:
            #3rd
            return 3
        else:
            #homerun
            return 4
    else:
        if r <= 0.284:
            #out
            return 0
        else:
            #stole base
            return q+1

q = 0
b0 = 0
b1 = 0
b2 = 0
b3 = 0
b4 = 0
for x in range(0,1000):
    q = next_state(q)
    if q == 0:
        b0 = b0 + 1
    elif q == 1:
        b1 = b1 + 1
    elif q == 2:
        b2 = b2 + 1
    elif q == 3:
        b3 = b3 + 1
    else:
        b4 = b4 + 1

print ("P(0)=",b0/1000.0)
print ("P(1)=",b1/1000.0)
print ("P(2)=",b2/1000.0)
print ("P(3)=",3/1000.0)
print ("P(4)=",b4/1000.0)

#5.2