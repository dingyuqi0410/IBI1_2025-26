import numpy as np
import matplotlib.pyplot as plt

population=np.zeros((100,100))
outbreak=np.random.choice(range(100),2)      #生成 0~99这100个数字，随机选两个数字
population[outbreak[0],outbreak[1]]=1      #把第outbreak[0]行，第outbreak[1]列位置的数值改成1（相当于给了一个坐标）

beta=0.3
gamma=0.05

# pseudocode
# repeat for 100 time steps
#     make a copy of the current population
#     find all infected individuals
#     for each infected individual:
#         check all 8 neighbours
#         if a neighbour is susceptible, infect it with probability beta
#         allow the infected individual to recover with probability gamma
#     replace the old population with the updated one
#     plot the result

times_to_plot=[0,10,50,100]
plt.figure(figsize=(6,4),dpi=150)
plot_number=1
plt.subplot(2, 2, plot_number)        #2，2把画布切成两行两列四个格子，选中第plot_number个格子，准备画图
plt.imshow(population, cmap='viridis', interpolation='nearest')
plt.title("time = 0")
plot_number+=1

for t in range (1,101):
    new_population=population.copy()     #要基于“当前时刻”的状态统一更新，所以要用copy，不能一边感染一边直接改原数组，否则同一个时间点里后改的数据可能影响前面的判断。
    infectedIndex=np.where(population==1)       #找到所有population=1（已感染）的坐标
    for i in range(len(infectedIndex[0])):      #遍历每一个感染者的x坐标（x坐标可以有重复的，所以不用担心一行有多个感染者的情况），如果不用[0]，直接用infectedIndex[0]，代表的是x坐标和y坐标两个大的数组
        x=infectedIndex[0][i]     #infectedIndex[0]代表所有感染者的x坐标，加[i]代表取出第i个感染者的x坐标
        y=infectedIndex[1][i]
        #尝试感染每个感染点的8个邻居
        for dx in [-1,0,1]:    #dx表示x坐标的变化
            for dy in [-1,0,1]:      #dy表示y坐标的变化
                if dx == 0 and dy == 0:     #跳过自己（不会感染自己）
                    continue
                new_x= x + dx
                new_y = y + dy
                if 0 <= new_x < 100 and 0 <= new_y < 100:     #判断坐标是否在（100，100）内，防止越界
                    if population[new_x, new_y] == 0:     #确定此时是未感染者
                        infect = np.random.choice([0, 1], p=[1 - beta, beta])     #有beta的概率被感染 
                        if infect == 1:      #如果中了概率被感染了
                            new_population[new_x, new_y] = 1      #原来的0换成1
        #感染者有gamma的概率能够康复
        recover=np.random.choice([0, 1], p=[1 - gamma, gamma])
        if recover==1:
            new_population[x,y]=2    #中了概率康复的换成2
    population=new_population       #更新人口

    if t in times_to_plot:
        plt.subplot(2, 2, plot_number)        #2，2把画布切成两行两列四个格子，选中第plot_number个格子，准备画图
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.title(f"time = {t}")
        plot_number += 1

plt.tight_layout()      #避免图重叠
plt.show()