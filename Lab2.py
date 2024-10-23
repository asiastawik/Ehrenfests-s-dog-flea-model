import numpy as np
import matplotlib.pyplot as plt
import random as rnd

p = float(input("Enter the value of p (from 0 to 1): "))
N = int(input("Enter the N number of fleas on REX (from 0 to 10^6): "))
t_sym = int(input("Enter the simulation time: "))

#Generate lists
fleas = np.ones(N)
time = np.arange(t_sym) #range of time
N_R = np.zeros(t_sym)
N_A = np.zeros(t_sym)
N_R[0] = N #first value is N, because all fleas is on REX
N_A[0] = 0 #0 fleas is on AXE

#Simulate the model
for t in time:
    flea = np.random.randint(0, N)
    p_random = np.random.rand()
    #flip the element with probability p
    if p_random < p:
        fleas[flea] = 1 - fleas[flea]

    N_R[t] = fleas.sum()
    N_A[t] = N - N_R[t]

#Saving file
file = "N" + str(N) + "p" + str(p) + "t" + str(t_sym) + ".txt"

with open(str(file), 'w') as f:
    for t in time:
        f.write(str(t))
        f.write('  ')
        f.write(str(N_R[t]))
        f.write('  ')
        f.write(str(N_A[t]))
        f.write('  ')
        f.write('\n')

# Plot the results
x = np.arange(t_sym)
plt.plot(x, N_R, label="REX")
plt.plot(x, N_A, label="ACE")
plt.xlabel("Time")
plt.ylabel("Number of fleas")
plt.legend()
plt.show()

'''
Repeat it for several values of N - conclusions:
If number of fleas are low (e.g. 100) the fleas jump on REX and then jump back on ACE and so on.
If number of fleas are large (e.g. 10000) all of fleas won't jump on REX due to lack of time.
If we change the probability it is also influence the result, because it changes the total time. 
The lower probability is the slower fleas jump on the other dog.
When the simulation time will be too low, fleas won't make it to jump on the other dog.

After some time, the number of fleas on each dog should be similar.
'''