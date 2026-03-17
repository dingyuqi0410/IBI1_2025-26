import matplotlib.pyplot as plt
#step 1
population_2020={"UK": 66.7,"China": 1426,"Italy": 59.4,"Brazil": 208.6,"USA": 331.6}
population_2024={"UK": 69.2,"China": 1410,"Italy": 58.9,"Brazil": 212.0,"USA": 340.1}
change={}      #创建一个空字典，用来存放变化
for country in population_2020:
    percentage_change=((population_2024[country] - population_2020[country]) / population_2020[country]) * 100
    print(f"percentage change of {country}: {percentage_change}")
    change[country]=percentage_change     #将变化存进字典change
#step 2
#怎么按照降序排列？
print(f"The largest increase: {max(change,key=change.get)}")
print(f"The largest decrease: {min(change,key=change.get)}")
#step 3
countries=list(change.keys())
changes=list(change.values())
plt.bar(countries,changes,width=0.35)
plt.ylabel('Percentage changes of population')
plt.xlabel('Countries')
plt.title('Population Growth Rate')
plt.show()