import numpy as np
import matplotlib.pyplot as plt

S=9999      # "S" for susceptible
I=1         # "I" for infected
R=0         # "R" for recovered
N=10000
beta=0.3
gamma=0.05
S_values=[S]
I_values=[I]
R_values=[R]

# pseudocode
# repeat for 1000 time steps
#     calculate infection probability = beta * I / N
#     randomly decide how many susceptible people become infected
#     randomly decide how many infected people recover
#     update S,I and R
#     save the new values in the lists
for t in range(1000):
    infection_probability=beta*I/N
    new_infections=np.random.choice([0,1],size=S,p=[1-infection_probability,infection_probability]).sum()      
    new_recoveries=np.random.choice([0,1],size=I,p=[1-gamma,gamma]).sum()
    S-=new_infections
    I=I+new_infections-new_recoveries
    R+=new_recoveries
    S_values.append(S)      
    I_values.append(I)
    R_values.append(R)

plt.figure(figsize=(6,4),dpi=150)
plt.plot(S_values,label="susceptible")
plt.plot(I_values,label="infected")
plt.plot(R_values,label="recovered")
plt.xlabel("Time")
plt.ylabel("Number of people")
plt.title("SIR Model")
plt.legend()
plt.savefig("SIR_model_plot.png",format='png')
plt.show()