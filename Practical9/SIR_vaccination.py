import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

N=10000
beta=0.3
gamma=0.05
plt.figure(figsize=(6,4),dpi=150)
for rate in range(0,101,10):            #从0开始到101（不包括101），步长为10，所以会生成0，10，20，30，40，50，60，70，80，90
    vaccination_rate=rate/100
    V=int(N*vaccination_rate)       #此时打了疫苗的人数，int()取整
    S=N-V-1
    I=1
    R=0
    I_values=[I]

    for t in range(1000):
        if S>0:
            infection_probability=beta*I/N
            new_infections=np.random.choice([0,1],size=S,p=[1-infection_probability,infection_probability]).sum()      #对每一个易感者随机决定“感染(1)”还是“不感染(0)”，把所有1加起来，就是新增的感染的人数
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
    plt.plot(I_values, color=cm.viridis(rate*3), label=f"{rate}%")         #color用了guidance给的配色方案

plt.xlabel("time")
plt.ylabel("number of people")
plt.title("SIR model with different vaccination rates")
plt.legend()
plt.savefig("SIR_vaccination_plot.png")
plt.show()

#"/Users/a18274964300/Documents/大一下/IBI1/IBI1_2025-26/IBI1_2025-26/Practical9/SIR_vaccination_plot",format="pn“