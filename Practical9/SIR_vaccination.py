import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

N=10000
beta=0.3
gamma=0.05
plt.figure(figsize=(6,4),dpi=150)
for rate in range(0,101,10):            
    vaccination_rate=rate/100
    V=int((N-1)*vaccination_rate)       
    S=N-V-1
    I=1
    R=0
    I_values=[I]

    for t in range(1000):
        if S>0:
            infection_probability=beta*I/N
            new_infections=np.random.choice([0,1],size=S,p=[1-infection_probability,infection_probability]).sum()     
        else:
            new_infections=0
        if I>0:
            new_recoveries=np.random.choice([0,1],size=I,p=[1-gamma,gamma]).sum()
        else:
            new_recoveries=0
        S-=new_infections
        I=I+new_infections-new_recoveries
        R+=new_recoveries
        I_values.append(I)
    plt.plot(I_values, color=cm.viridis(rate*3), label=f"{rate}%")         

plt.xlabel("Time")
plt.ylabel("Number of infected people")
plt.title("SIR Model with different vaccination rates")
plt.legend()
plt.savefig("SIR_vaccination_plot.png",format='png')
plt.show()