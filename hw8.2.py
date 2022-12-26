from __future__ import absolute_import, division, print_function
import simpy 
import matplotlib.pyplot as plt
import numpy as np

#8.2 Factory Problem

def factory_run(env, repairers, spares):
    #define global variables for inter-process communicaton
    global cost 
    cost = 0

    #launch the 50 machine processes 
    for i in range(50):
        env.process(operate_machine(env, repairers, spares))
        #update the daily costs each day
    while True:
        cost+=3.75*8*repairers.capacity + 30*spares.capacity
        yield env.timeout(8.0)

def operate_machine(env, repairers, spares):
    #define global variables for the inter-process communication
    global cost 
    while True:
        #wait until the machine breaks
        yield env.timeout(np.random.uniform(132, 182))
        time_broken = env.now
        #launch repair process
        env.process(repair_machine(env, repairers, spares))
        #wait for a spair to become available
        yield spares.get(1)
        time_replaced = env.now
        #update the cost for being out of service
        cost += 20*(time_replaced -time_broken)

def repair_machine(env, repairers, spares):
    #process to repair a machine
    with repairers.request() as request:
        yield request
        #perform the repair
        yield env.timeout(np.random.uniform(4,10))
        #put the machine back in the spares pool
        yield spares.put(1)
def observe(env, spares):
    #Process to observe the factory during a simulation
    while True:
        obs_time.append(env.now)
        obs_cost.append(cost)
        obs_spares.append(spares.level)
        yield env.timeout(1.0)

#create the simulation environment
env = simpy.Environment()

#create arrays to record data
obs_time = []
obs_cost = []
obs_spares = []

#create the resources
repairers = simpy.Resource(env, capacity=4) #trial and error
spares = simpy.Container(env, init=10, capacity=15)

#add the factory run process
env.process(factory_run(env, repairers, spares))
#add an observation process
env.process(observe(env,spares))
#run simulation
env.run(until=8*5*52)

print('Total cost: {:.2f}'.format(cost))

#plot the number of spares available
plt.figure()
plt.step(obs_time, obs_spares, where='post')
plt.xlabel('Time(hour)')
plt.ylabel('Numer of Spares Available')

#Plot the tital cost accumulation
plt.figure()
plt.step(obs_time, obs_cost, where='post')
plt.xlabel('Time(hour)')
plt.ylabel('Total Cost')
plt.show()
print("Average number of spares available: ", np.average(obs_spares))

#   MONTE CARLO SIMULATION
NUM_RUNS = 10
NUM_SPARES = 15
NUM_REPAIRERS = 3 

#array to store outputs 
COST = []

for i in range(NUM_RUNS):
    #set the random seed
    np.random.seed(i)

    #create the simpy environment
    env = simpy.Environment()

    #create arrays to record data 
    obs_time = []
    obs_cost = []
    obs_spares = []

    #create resources
    repairers = simpy.Resource(env, capacity=NUM_REPAIRERS) 
    spares = simpy.Container(env, init=NUM_SPARES, capacity=NUM_SPARES)
    
    # add the factory run process
    env.process(factory_run(env, repairers, spares))
    
    # add the observation process
    env.process(observe(env, spares))
    
    # run simulation
    env.run(until=5*8*52)
    
    # record the final cost
    COST.append(cost)


# print final results to console
print('Factory costs for N={:} runs with R={:} repairers and S={:} spares:'.format(
        NUM_RUNS, NUM_REPAIRERS, NUM_SPARES))
print('\n'.join('{:.2f}'.format(i) for i in COST))
print('95th Percentile OF BALANCE = {:.0f}'.format(np.percentile(COST,95)))
print('5th Percentile of Balance = {:.0f}'.format(np.percentile(COST, 5)))
print('95th Percentile of Inventory Level = {:.0f}'.format(np.percentile(obs_spares, 95)))
print('5th Percentile of Inventory Level = {:.0f}'.format(np.percentile(obs_spares, 5)))