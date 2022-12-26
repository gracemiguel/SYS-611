from __future__ import absolute_import, division, print_function
import simpy
import numpy as np
import matplotlib.pyplot as plt


def warehouse_run(env, order_threshold, max_order):
    global inventory, balance, num_ordered
    inventory = max_order
    balance = 0 
    num_ordered = 0
    while True:
        interarrival = np.random.exponential(1/5.0)
        yield env.timeout(interarrival)
        balance -= 2.00*inventory*interarrival
        demand = np.random.randint(1,4)
        if inventory > demand:
            num_sold = demand
        else:
            num_sold = inventory
        balance+=100.0*num_sold
        inventory -=num_sold
        if inventory < order_threshold and num_ordered == 0:
            env.process(handle_order(env, max_order-inventory))

def handle_order(env, quantity):

    global inventory, balance, num_ordered
    num_ordered = quantity
    balance -=50.00*quantity
    yield env.timeout(2.0)
    inventory += quantity
    num_ordered = 0



def observe(env):
    while True:
        #record the observation time and queue length
        obs_time.append(env.now)
        inventory_level.append(inventory)
        yield env.timeout(0.1)

obs_time = []
inventory_level = []

env = simpy.Environment()
env.process(warehouse_run(env, 35, 70))
env.process(observe(env))
env.run(until=100.0)
print('ending inventory_level', inventory_level[len(inventory_level)-1])
# plot the inventory over time
plt.figure()
plt.step(obs_time, inventory_level, where='post')
plt.xlabel('Time (day)')
plt.ylabel('Inventory Level')
plt.show()


#MONTE CARLO
NUM_RUNS = 10
ORDER_THRESHOLD = 35
MAX_ORDER = 70

#array to store outputs
BALANCE = []

for i in range(NUM_RUNS):
    #Set the initial seed
    np.random.seed(i)

    #create the simulation environment
    env = simpy.Environment()

    #create arrays to record data
    obs_time = []
    obs_inventory = []

    #add the warehouse run process
    env.process(warehouse_run(env, ORDER_THRESHOLD, MAX_ORDER ))

    #Add the observation process
    env.process(observe(env))

    #run the simulation
    env.run(until=100)

    #record the final observed net revenue
    BALANCE.append(balance)

    obs_inventory.append(inventory_level)
#print final results 
print('Net revenude balance for N={:} runs with Q={:} and S={:}'.format(NUM_RUNS, ORDER_THRESHOLD, MAX_ORDER))
print('\n'.join('{:.2f}'.format(i) for i in BALANCE))
print("average balance", np.average(BALANCE))
print('95th Percentile OF BALANCE = {:.0f}'.format(np.percentile(BALANCE,95)))
print('5th Percentile of Balance = {:.0f}'.format(np.percentile(BALANCE, 5)))
print('95th Percentile of Inventory Level = {:.0f}'.format(np.percentile(inventory_level, 95)))
print('5th Percentile of Inventory Level = {:.0f}'.format(np.percentile(inventory_level, 5)))


