import numpy as np
import matplotlib.pyplot as plt

population=np.zeros((100,100))        #set up a 100x100 grid representing the population, initially all susceptible (0)
outbreak=np.random.choice(range(100),2)      #generate 0~99 these 100 numbers, randomly select two numbers, will generate an array, such as [15,42]表示第15行，第42列
population[outbreak[0],outbreak[1]]=1      #change the value at the position of the outbreak[0] row and outbreak[1] column to 1 (equivalent to giving a coordinate)

beta=0.3    #infection probability
gamma=0.05     #recovery probability

#draw the initial state of the population
plt.figure(figsize=(6, 4), dpi=150)    
plt.imshow(population, cmap="viridis", interpolation="nearest")
plt.title("Spatial SIR Model at Time 0")
plt.xlabel("X coordinate")
plt.ylabel("Y coordinate")
plt.tight_layout()
plt.show()

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

for t in range (1,101):
    new_population=population.copy()     
    infectedIndex=np.where(population==1)       
    for i in range(len(infectedIndex[0])):      
        x=infectedIndex[0][i]    
        y=infectedIndex[1][i]

        for dx in [-1,0,1]:    
            for dy in [-1,0,1]:      
                if dx == 0 and dy == 0:     
                    continue
                new_x= x + dx
                new_y = y + dy
                if 0 <= new_x < 100 and 0 <= new_y < 100:     
                    if population[new_x, new_y] == 0:     
                        infect = np.random.choice([0, 1], p=[1 - beta, beta])     
                        if infect == 1:      
                            new_population[new_x, new_y] = 1      
        
        recover=np.random.choice([0, 1], p=[1 - gamma, gamma])
        if recover==1:
            new_population[x,y]=2    
    population=new_population       

    plt.figure(figsize=(6, 4), dpi=150)
    plt.imshow(population, cmap="viridis", interpolation="nearest")      
    plt.title(f"Spatial SIR Model at Time {t}")
    plt.xlabel("X coordinate")
    plt.ylabel("Y coordinate")
    plt.tight_layout()   
    plt.show()    