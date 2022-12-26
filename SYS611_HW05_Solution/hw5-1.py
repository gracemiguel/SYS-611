# -*- coding: utf-8 -*-
"""
SYS-611 HW5.1: Ty Cobb's Markov Model.

@author: Paul T. Grogan, pgrogan@stevens.edu
"""

# import the numpy package and refer to it as `np`
# see http://docs.scipy.org/doc/numpy/reference/ for documentation
import numpy as np

# define the state transition function
def next_state(r, q):
    # if currently in state 0, use batting process generator
    if q == 0:
        if r < 364/700.:
            # got out
            return 0
        elif r < (364+289)/700.:
            # got a single
            return 1
        elif r < (364+289+31)/700.:
            # got a double
            return 2
        elif r < (364+289+31+13)/700.:
            # got a triple
            return 3
        else:
            # got a home run
            return 4
    # if currently at home, return to bench
    elif q == 4:
        return 0
    # otherwise use baserunning process generator
    else:
        if r < 38/134.:
            # caught stealing
            return 0 
        else:
            # stole the base
            return q + 1

# allocate arrays to store state trajectory, also store random numbers
num_samples = 1000
q = np.zeros(num_samples)
np.random.seed(0)
r = np.random.rand(num_samples)
# override with provided values
r[0] = 0.765
r[1] = 0.557
r[2] = 0.347
r[3] = 0.098
r[4] = 0.039
r[5] = 0.132

# compute all the state updates
for t in range(num_samples - 1):
    q[t+1] = next_state(r[t], q[t])

# print results for the first 5 time steps
print '{:^5}{:^5}{:^5}'.format('t', 'q(t)', 'q(t+1)')
for t in range(6):
    print '{:^5d}{:^5.0f}{:^5.0f}'.format(t, q[t], q[t+1])

# print stationary distribution estimate
for i in range(5):
    print 'pi[{:}] = {:.3f}'.format(i, np.sum(q==i)/float(num_samples))