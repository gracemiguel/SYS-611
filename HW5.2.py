# -*- coding: utf-8 -*-
"""
SYS-611 Queuing Markov Model Example

@author: Paul T. Grogan, pgrogan@stevens.edu
"""

# import the python3 behavior for importing, division, and printing in python2
from __future__ import absolute_import, division, print_function

# import the numpy package and refer to it is `np`
import numpy as np
# import the matplotlib pyplot package and refer to it is `plt`
import matplotlib.pyplot as plt

_lambda = 0.5 # arrival rate, 1.5 minutes per customer or 2/3 customer per minute
A_mu = 2/3 # service rate, for Associate A
B_mu= 5/6 # service rate for Associate B

# define process generator for inter-arrival duration
def gen_t_arrival():
    r = np.random.rand()
    return -np.log(1-r)/_lambda
    # note: could also use
    # return np.random.exponential(scale=1/_lambda)

# define process generator for service duration for Associate A
def gen_t_service_a():
    r = np.random.rand()
    return -np.log(1-r)/A_mu
    # note: could also use
    # return np.random.exponential(scale=1/_mu)
    
# define process generator for service duration for Associate A
def gen_t_service_b():
    r = np.random.rand()
    return -np.log(1-r)/B_mu
    # note: could also use
    # return np.random.exponential(scale=1/_mu)
# define the number of events
NUM_EVENTS = 1000
# create lists to store variables of interest
t = np.zeros(NUM_EVENTS+1) # time
q = np.zeros(NUM_EVENTS+1) # number of customers in system
B_t = np.zeros(NUM_EVENTS+1) # time
B_q = np.zeros(NUM_EVENTS+1) # number of customers in system
A_b = np.zeros(NUM_EVENTS)   #how long the cashier is busy
A_c = np.zeros(NUM_EVENTS)   #number of new customer arrivals
A_w = np.zeros(NUM_EVENTS)   # waiting time incurred during an event
B_b = np.zeros(NUM_EVENTS)   #how long the cashier is busy
B_c = np.zeros(NUM_EVENTS)   #number of new customer arrivals
B_w = np.zeros(NUM_EVENTS)   # waiting time incurred during an event
t_arrival = np.zeros(NUM_EVENTS) # sampled inter-arrival durations
B_t_arrival = np.zeros(NUM_EVENTS) # sampels inter-arribal durations for associate B
t_service_a = np.zeros(NUM_EVENTS) # sampled service durations
t_service_b = np.zeros(NUM_EVENTS)
delta_t = np.zeros(NUM_EVENTS) # duration of each event
B_delta_t = np.zeros(NUM_EVENTS) #duration of each event for Associate B

# initialize time and state variables
t[0] = 0
q[0] = 0

for i in range(NUM_EVENTS):
    # generate samples for inter-arrival and service durations
    t_arrival[i] = gen_t_arrival()
    t_service_a[i] = gen_t_service_a()
    # process state transitions / updates for q and t
    if q[i] == 0 or t_arrival[i] < t_service_a[i]:
        # if no customers in queue or arrival happens before service
        # event is an arrival
        delta_t[i] = t_arrival[i]
        q[i+1] = q[i] + 1
    else:
        # otherwise event is a service
        delta_t[i] = t_service_a[i]
        q[i+1] = q[i] - 1
    t[i+1] = t[i] + delta_t[i]
    if q[i] > 0:
        A_b[i] = delta_t[i]
    else:
        A_b[i] = 0
    if delta_t[i] == t_arrival[i]:
        A_c[i] = 1
    else:
        A_c[i] = 0
    A_w[i] = q[i]*delta_t[i]
    

A_ro = sum(A_b)/sum(delta_t)
A_avg_waiting_time = sum(A_w)/sum(A_c)
# print('{:>10s}{:>10s}{:>10s}{:>10s}{:>10s}{:>10s}{:>10s}'.format(
#         'i', 't(i)', 'q(i)', 't_arrival', 't_service_a', 'delta_t', 'q(i+1)'))
# for i in range(NUM_EVENTS):
#     print('{:10.0f}{:10.2f}{:10.0f}{:10.2f}{:10.2f}{:10.2f}{:10.0f}'.format(
#             i, t[i], q[i], t_arrival[i], t_service_a[i], delta_t[i], q[i+1]))
print("Utilization rato for Associate A", A_ro )
print("Average Waiting Time for Associate A", A_avg_waiting_time)

for i in range(NUM_EVENTS):
    # generate samples for inter-arrival and service durations
    B_t_arrival[i] = gen_t_arrival()
    t_service_b[i] = gen_t_service_b()
    # process state transitions / updates for q and t
    if B_q[i] == 0 or B_t_arrival[i] < t_service_b[i]:
        # if no customers in queue or arrival happens before service
        # event is an arrival
        B_delta_t[i] = B_t_arrival[i]
        B_q[i+1] = B_q[i] + 1
    else:
        # otherwise event is a service
        B_delta_t[i] = t_service_b[i]
        B_q[i+1] = B_q[i] - 1
    B_t[i+1] = B_t[i] + B_delta_t[i]
    if B_q[i] > 0:
        B_b[i] = B_delta_t[i]
    else:
        B_b[i] = 0
    if B_delta_t[i] == B_t_arrival[i]:
        B_c[i] = 1
    else:
        B_c[i] = 0
    B_w[i] = B_q[i]*B_delta_t[i]

B_ro = sum(B_b)/sum(B_delta_t)
B_avg_waiting_time = sum(B_w)/sum(B_c)
    
print("Utilization ratio for Associate B",B_ro)
print("Average Waiting Time for Associate B", B_avg_waiting_time)
plt.figure()
plt.xlabel('Time, $t$')
plt.ylabel('Customers in System, $q$')
plt.step(t,q,'-r',where='post')