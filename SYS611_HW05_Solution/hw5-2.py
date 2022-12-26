# -*- coding: utf-8 -*-
"""
SYS-611 HW5.2: Cafe Java Cashier.

@author: Paul T. Grogan, pgrogan@stevens.edu
"""

# import the python3 behavior for importing, division, and printing in python2
from __future__ import absolute_import, division, print_function

# import the numpy package and refer to it is `np`
import numpy as np

_lambda = 30/60 # arrival rate, 20 per hour or 1/2 per minute
_mu_A = 1/1.5 # service rate, 1.5 minutes each or 2/3 per minute
_mu_B = 1/1.2 # service rate, 1.2 minutes each or 5/6 per minute

_mu = _mu_B

# define process generator for inter-arrival duration
def gen_t_arrival():
    r = np.random.rand()
    return -np.log(1-r)/_lambda
    # note: could also use
    # return np.random.exponential(scale=1/_lambda)

# define process generator for service duration
def gen_t_service():
    r = np.random.rand()
    return -np.log(1-r)/_mu
    # note: could also use
    # return np.random.exponential(scale=1/_mu)
    
# define the number of events
NUM_EVENTS = 10000
# create lists to store variables of interest
q = np.zeros(NUM_EVENTS+1)
t = np.zeros(NUM_EVENTS+1)
t_arrival = np.zeros(NUM_EVENTS)
t_service = np.zeros(NUM_EVENTS)
delta_t = np.zeros(NUM_EVENTS)
c = np.zeros(NUM_EVENTS)
b = np.zeros(NUM_EVENTS)
w = np.zeros(NUM_EVENTS)

# reset random number seed for consistent results
np.random.seed(0)

# initialize time and state variables
t[0] = 0
q[0] = 0

for i in range(NUM_EVENTS):
    # generate samples for inter-arrival and service durations
    t_arrival[i] = gen_t_arrival()
    t_service[i] = gen_t_service()
    # if no customers in queue or arrival happens before service
    if q[i] == 0 or t_arrival[i] < t_service[i]:
        # event is an arrival
        delta_t[i] = t_arrival[i]
        q[i+1] = q[i] + 1
    else:
        # otherwise event is a service
        delta_t[i] = t_service[i]
        q[i+1] = q[i] - 1
    t[i+1] = t[i] + delta_t[i]
    # record derived state variables
    b[i] = delta_t[i] if q[i] > 0 else 0
    c[i] = 1 if delta_t[i] == t_arrival[i] else 0
    w[i] = q[i] * delta_t[i]

rho = np.sum(b)/np.sum(delta_t)
W_bar = np.sum(w)/np.sum(c)

print('rho = {:.3f}'.format(rho))
print('W_bar = {:.2f}'.format(W_bar))