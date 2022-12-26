#Grace Miguel
# November, 10, 2021
#HW7 

import numpy as np
import math
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import mean
#7.1
#a

NUM_SAMPLES = 1000

target_vol = 500*(.68/.636)
lwr_jar =target_vol - target_vol*.05
upper_jar = target_vol + target_vol*.15
jar_vol = np.random.triangular(lwr_jar,target_vol,upper_jar, NUM_SAMPLES)
mean_jar = np.mean(jar_vol)
print("mean jar vol", mean_jar)



target_pf = 0.68
lwr_packing = target_pf -.2*target_pf
upper_packing = target_pf+ .2*target_pf
packing_factor = np.random.triangular(lwr_packing, target_pf, upper_packing, NUM_SAMPLES)
    


target_mm_d = 1.4 #cm
lwr_mm_d = target_mm_d - target_mm_d*.1
upper_mm_d = target_mm_d + target_mm_d*.1
mm_d = np.random.triangular(lwr_mm_d, target_mm_d, upper_mm_d, NUM_SAMPLES)



target_mm_t = .635
lwr_mm_t = target_mm_t - target_mm_t*.1
upper_mm_t = target_mm_t + target_mm_t*.1
mm_t = np.random.triangular(lwr_mm_t, target_mm_t, upper_mm_t, NUM_SAMPLES)
    
mm_volume = (math.pi/6)*(mm_d)*(mm_d)*mm_t
print(mm_volume)
mms_in_jar = (packing_factor*jar_vol)/mm_volume
#b
# seed the random number generator for consistent results
np.random.seed(0)
# create the histogram plot
plt.figure()
plt.hist(mms_in_jar,color='red')
plt.xlabel('Number of M&Ms')
plt.ylabel('Frequency')
plt.savefig('mm_in_jar.png')


# output the descriptive statistics
print('Sample mean: {:.1f} m&ms'.format(np.mean(mms_in_jar)))
print('95th percentile: {:.1f} m&ms'.format(np.percentile(mms_in_jar,95)))


#7.2




