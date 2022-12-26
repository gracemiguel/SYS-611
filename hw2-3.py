# -*- coding: utf-8 -*-
"""
Solution for SYS-611 HW02.3

@author: Paul T. Grogan, pgrogan@stevens.edu
"""

# import the python3 behavior for importing, division, and printing in python2
from __future__ import absolute_import, division, print_function

# import the numpy package and refer to it as `np`
# see http://docs.scipy.org/doc/numpy/reference/ for documentation
import numpy as np

# import the matplotlib pyplot package and refer to it as `plt`
# see http://matplotlib.org/api/pyplot_api.html for documentation
import matplotlib.pyplot as plt


#%% problem 2.3(a)

# seed the random number generator to get consistent results
np.random.seed(0)

# rate parameter for customers per minute
_lambda = 2.0

# create a function for a continuous process generator
def gen_sample():
    r = np.random.rand()
    return -np.log(1-r)/_lambda

# generate array with 1000 samples
samples = np.array([gen_sample() for i in range(1000)])

plt.figure()
plt.hist(samples, color='r')
plt.xlabel('z')
plt.ylabel('Frequency')
plt.savefig('hw2-3a.png')


#%% problem 2.3(b)

# compute the arrival times from the inter-arrival samples
arrival = np.cumsum(samples)

# display the first 10 arrivals to help debug
print('{:2s} {:10s} {:10s}'.format('i', 'Sample z_i', 'Arrival t_i'))
for i in range(10):
    print('{:2d} {:10.2f} {:10.2f}'.format(i+1, samples[i], arrival[i]))
print()

#%% problem 2.3(c)

# create a list of the 300 1-minute time intervals
interval = np.arange(0,300,1)
# count how many customers arrive during each interval
counts = np.array([np.sum(np.logical_and(arrival >= i, arrival < i + 1)) for i in interval])

# display the first 5 intervals to help debug
print('{:9s} {:6s}'.format('Interval', 'Count'))
for i in range(5):
    print('{:4.1f}-{:4.1f} {:6d}'.format(i,i+1,counts[i]))
print()

plt.figure()
plt.hist(counts, bins=range(11), color='r')
plt.xlabel('k')
plt.ylabel('Frequency')
plt.savefig('hw2-3c.png')

