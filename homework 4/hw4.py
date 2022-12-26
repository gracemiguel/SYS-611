#Grace Miguel
#October 19,2021
import scipy.integrate.quadpack
import scipy.integrate.odepack
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,180, num=900)

S = np.zeros(900)
S[0]=1600-1
I=np.zeros(900)
I[0]=1
R=np.zeros(900)
R[0]= 0

delta_t = 0.2
gamma = 0.1
N=1600
beta= .2
for i in range(900):
    if i == 899:
        break
    S[i+1]=S[i] + delta_t*(-beta*S[i]*(I[i]/N))
    I[i+1]=I[i] + delta_t*(beta*S[i]*(I[i]/N) - gamma*I[i])
    R[i+1]= R[i]+ delta_t*gamma*I[i]

infected_day = np.argmax(I)
infected = np.amax(I)
print(f"On day {infected_day}, {infected} were infected")
remov_pop = R[899]
dead = remov_pop*.02
print("this many are dead" , dead)

plt.figure()
plt.step(t, S, '-r', where='post', label='Susceptible Population')
plt.step(t,I,'b', where='post', label="Infectious Population" )
plt.step(t, R, "y", where="post", label="Removed Population")
plt.xlabel('Time ($t$)')
plt.ylabel('Population Size $(persons)$')
plt.title("COVID-19 Infection Rates")
plt.legend(loc='best')




 



