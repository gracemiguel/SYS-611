import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

die_nums = np.array([1,2,3,4,5,6])
possibility = np.array([11/36,9/36,7/36,5/36,3/36,1/36])
pmf = possibility/np.sum(possibility)
cdf=np.cumsum(pmf)
print(cdf)

def gen_demand_ivt():
    r=np.random.rand()
    for i in range(len(die_nums)):
        if r <=cdf[i]:
            return i
print(gen_demand_ivt())
samples_ivt = [gen_demand_ivt() 
    for i in range(1000)]

print(samples_ivt)
data = pd.DataFrame(samples_ivt, columns=['x', 'y'])
counts = np.array([sum(samples_ivt==i) for i in die_nums])
possibility_ivt = counts/np.sum(counts)


for col in 'xy':
    plt.hist(data[col], normed=True)
# possibility_ivt = counts/np.sum(counts)

