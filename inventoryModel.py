"""
SYS-611 Inventory Model

@author: Paul T. Grogan, pgrogan@stevens.edu
"""

# import the python3 behavior for importing, division, and printing in python2
from __future__ import absolute_import, division, print_function

# import the numpy package and refer to it as `np`
import numpy as np
import math
import scipy.stats as stats
# import the matplotlib.pyplot package and refer to it as `plt`
import matplotlib.pyplot as plt
from numpy.core.numeric import Infinity



confidence_level = 0.05
z_crit = stats.norm.ppf(1-confidence_level/2)
time = [0]
adj_inventory = [40]
inventory = 40
penalty = 0

NUM_SIMULATIONS = 260
t_delivery = math.inf
#DPG for demand
def generate_demand():
    demand = np.random.rand()
    if demand < 0.13:
        return 2
    elif demand >= 0.13 and demand <0.55:
        return 3
    else:
        return 5


#CPG for lead time
def generate_leadtime():
    rs = np.random.rand()
    return int(5+ -np.log(1-rs)/.25)


for i in range(NUM_SIMULATIONS):
    demand = generate_demand()
    if inventory < demand:
        penalty+= demand-inventory
    if t_delivery == math.inf:
        if inventory < 30:
            t_delivery = generate_leadtime()
            inventory-=demand
        else:
            inventory-=demand
    elif t_delivery == 0:
        t_delivery = math.inf
        inventory = (inventory - demand + 40)
    else:
        t_delivery -=1
        inventory-=demand
    time.append(i)
    adj_inventory.append(inventory)

plt.figure()
plt.plot(time, adj_inventory, '-r')
plt.xlabel('Time ($days$)')
plt.ylabel('Inventory')
print('p = {:.3f} +/- {:.3f} (95% CI)'.format(
        np.average(adj_inventory),
        z_crit*stats.sem(adj_inventory)
    ))
print(adj_inventory)
mean_estimate = np.array([np.average(adj_inventory[0:i]) for i in range(len(adj_inventory))])
confidence_int = z_crit*np.array([stats.sem(adj_inventory[0:i]) for i in range(len(adj_inventory))])


# print("Upper bound of 95 percent confidence interval", mean_estimate+confidence_int)
# def generate_interarrival():
#     # generates a customer inter-arrival time
#     return np.random.exponential(scale=1./arrival_rate)
    
