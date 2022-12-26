#Grace Miguel
#Homework 3
#I pledge my honor that I've abided by the Stevens Honor System

from functools import total_ordering
import numpy as np
from numpy.core.arrayprint import ComplexFloatingFormat
import scipy.stats as stats
import matplotlib.pyplot as plt

# seed the random number generator to get consistent results
np.random.seed(0)
#this is for 3.1 part a
X = np.random.rand()
Y= np.random.rand()

Z = np.sqrt(X*X + Y*Y)
#3.1 part b
def gen_rice():
    X = np.random.rand()
    Y= np.random.rand()
    if(np.sqrt(X*X + Y*Y)) <=1:
        return 4
    else:
        return 0
    

# generate 10000 samples
samples = [gen_rice() for i in range(10000)]

# compute the lower and upper-bounds using a 95% confidence interval
confidence_level = 0.05
z_crit = stats.norm.ppf(1-confidence_level/2)
# compute running statistics for mean and confidence interval
mean_estimate = np.array([np.average(samples[0:i]) for i in range(len(samples))])
confidence_int = z_crit*np.array([stats.sem(samples[0:i]) for i in range(len(samples))])

print('pi = {:.3f} +/- {:.3f} (95% CI)'.format(
        np.average(samples),
        z_crit*stats.sem(samples)
    ))


#part c

def gen_rice2():
    X = np.random.rand()
    Y= np.random.rand()
    Z1 = np.sqrt(X*X + Y*Y)
    Z2 = np.sqrt(pow(1-X, 2)+ pow(1-Y, 2))
    z1 = 0
    z2 = 0
    if Z1 <=1:
        z1= 4
    else:
        z1= 0
    if Z2 <=1:
        z2 = 4
    else: 
        z2 = 0
    Z_a = (z1+z2)/2
    return Z_a


# generate 10000 samples
samples_2 = [gen_rice2() for i in range(10000)]

# compute the lower and upper-bounds using a 95% confidence interval
confidence_level = 0.05
z_crit = stats.norm.ppf(1-confidence_level/2)
# compute running statistics for mean and confidence interval
mean_estimate = np.array([np.average(samples_2[0:i]) for i in range(len(samples))])
confidence_int = z_crit*np.array([stats.sem(samples_2[0:i]) for i in range(len(samples))])

print('Antithetic derived pi = {:.3f} +/- {:.3f} (95% CI)'.format(
        np.average(samples),
        z_crit*stats.sem(samples)
    ))

#3.2 part a
LD = 1/3 *np.random.rand()
Weight = 1.3+.2*np.sqrt(np.random.rand())

#3.2 part b*
R = LD*.255*5950*np.log(Weight)

#3.2 part c 
#part i
def gen_aircraft():
    LD= 15+ np.random.rand()*3
    Weight = 1.3+.2*np.sqrt(np.random.rand())
    R = LD*.255*5950*np.log(Weight)
    return R

samples_air = [gen_aircraft() for i in range(1000)]
print("LENGTH OF SAMPLES AIR", len(samples_air))
print("type of samples_air", type(samples_air))
samples_array = np.array(samples_air)
plt.hist(samples_air, color="r", bins=3 )
plt.xlabel('Aircraft Range')
plt.ylabel('Frequency')
plt.show()
plt.savefig('hw3-2c.png')

#part c ii
mean = np.average(samples_air)
print("this is sample mean", mean)

#part c iii

percentile_25 = np.sort(samples_array)
print("this is the 25th percentile", percentile_25[249])


#part c iv
total_exceed = samples_array[samples_array >9000]
over_9000 = len(total_exceed)/len(samples_array)
print("probability of exceeding 9000km", over_9000)

#3.3 part a

a= 40
b = 70
c = 90


x=np.random.randint(40,90)


def f(x):
    if(x<=70 and x>40):
        return 2*(x-40)/((70-40)*(90-70))
    else:
        return  2*(90-x)/((90-40)*(90-70))

x=np.arange(40,90)
y = []


plt.show()
for i in range(len(x)):
   y.append(f(x[i]))
plt.plot(x,y,c="red")
# piecewise = np.piecewise(x, [x<=70, x>70], [2*(x-40)/((70-40)*(90-70)),  2*(90-x)/((90-40)*(90-70))])
# plt.plot(x,y)
plt.show()


#part d

def demand_generator():
    area = 3/5
    r = np.random.rand()

    if( r >= 0 and r<= area):
        x = 40+ np.sqrt(1500*r)
    else:
        x = 90 - np.sqrt(1000-1000*r)
    return x

demand_generator()

#part f

def profit_generator():
    orders = np.random.randint(40,70)
    demand = demand_generator()
    if demand <= orders:
        leftover = demand-orders
        profit = 12*demand + 3*leftover - 10*demand
    else: 
        profit = 12*demand - 10*demand
    return profit


samples_profit = [profit_generator() for i in range(1000)]
mean_profit = np.average(samples_profit)
print("This is the sample mean for profit", mean_profit)