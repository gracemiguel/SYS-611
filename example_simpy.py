import simpy 

#simulates a car driving
def car_run(env, t, q):
    while True:
        #enter driving state
        t.append(env.now)
        q.append(1)

        #wait 5.0hrs
        yield env.timeout(5.0)

        #enter parked state
        yield env.timeout(2.0)
#create the simulation environment
env = simpy.Environment()

t= []
q = []

#run the simulation for 15.0 hrs
env.run(until=15)
