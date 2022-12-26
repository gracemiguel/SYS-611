# -*- coding: utf-8 -*-
"""
Solution for SYS-611 HW02.2

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

# import the scipy stats package and refer to it as `stats`
# see http://docs.scipy.org/doc/scipy-0.14.0/reference/stats.html for docs
import scipy.stats as stats

#%% problem 2.2(a)

# seed the random number generator to get consistent results
np.random.seed(0)

# define the values of y using increments of 0.1
y = np.arange(0,15,0.1)

# define the pdf for f(y)
f = (y - 3)/18
# override values < 5 to zero
f[y<3] = 0
# override values > 10 to zero
f[y>9] = 0

# compute the cdf for F(y)
F = (y - 3)**2/36
# override values < 5 to zero
F[y<3] = 0
# override values > 15 to one
F[y>9] = 1

#%% problem 2.2(b)

# create a line plot for pdf
plt.figure()
plt.plot(y, f, '-r')
plt.xlabel('Time to Drink a Coffee, $y$')
plt.ylabel('Probability Density, $f(y)$')
plt.savefig('hw2-2b.png')

#%% problem 2.2(c)

# create a line plot for cdf
plt.figure()
plt.plot(y, F, '-r')
plt.xlabel('Time to Drink a Coffee, $y$')
plt.ylabel('Cumulative Probability Density, $F(y)$')
plt.savefig('hw2-2c.png')

#%% problem 2.2(d)

# create a function for a continuous process generator
def gen_sample():
    r = np.random.rand()
    return 6*np.sqrt(r) + 3

# generate array with 1000 samples
samples = np.array([gen_sample() for i in range(1000)])

# create a histogram of sampled values
plt.figure()
# use automatic bins and set color to red
plt.hist(samples, color='r')
plt.xlabel('Time to Drink a Coffee, $y$')
plt.ylabel('Frequency')
plt.show()
plt.savefig('hw2-2d.png')

# print out descriptive statistics and confidence interval
print('y_bar={:.2f}'.format(np.average(samples)))
print('s_y={:.2f}'.format(np.std(samples, ddof=1)))
print('95% CI mu_y=[{:.2f}, {:.2f}]'.format(
        np.average(samples)-stats.norm.ppf(1-0.05/2)*stats.sem(samples),
        np.average(samples)+stats.norm.ppf(1-0.05/2)*stats.sem(samples)))