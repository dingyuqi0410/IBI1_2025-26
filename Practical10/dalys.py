import os      
import pandas as pd       
import matplotlib.pyplot as plt
import numpy as np

os.chdir("/Users/a18274964300/Documents/大一下/IBI1/IBI1_2025-26/IBI1_2025-26/Practical10")   
print(os.getcwd())
print(os.listdir())

dalys_data=pd.read_csv("dalys-rate-from-all-causes.csv")

first_10_year_dalys=dalys_data.iloc[0:10,2:4]     
print(first_10_year_dalys)
max_dalys_first_10=first_10_year_dalys["DALYs"].max()    
max_year_first_10=first_10_year_dalys.loc[first_10_year_dalys["DALYs"]==max_dalys_first_10,"Year"].iloc[0]        
print(f"Year with maximum DALYs in the first 10 Afghanistan rows: {max_year_first_10}")     
# The year with the maximum DALYs across the first 10 recorded years for Afghanistan is: 1998

my_row = []   
for entity in dalys_data.loc[:, "Entity"]:      
    if entity == "Zimbabwe":
        my_row.append(True)
    else:
        my_row.append(False)
zimbabwe_years=dalys_data.loc[my_row,"Year"]      
print(zimbabwe_years)

first_zimbabwe_year=zimbabwe_years.min()
last_zimbabwe_year=zimbabwe_years.max()
print(f"First Zimbabwe year: {first_zimbabwe_year}")
print(f"Last Zimbabwe year: {last_zimbabwe_year}")
# The first year recorded: 1990; The last year recorded: 2019

recent_data=dalys_data.loc[dalys_data.Year==2019,["Entity","DALYs"]]
max_country=recent_data.loc[recent_data["DALYs"]==recent_data["DALYs"].max(),"Entity"].iloc[0]
print(f"Country with maximum DALYs in 2019: {max_country}")
min_country=recent_data.loc[recent_data["DALYs"]==recent_data["DALYs"].min(),"Entity"].iloc[0]
print(f"Country with minimum DALYs in 2019: {min_country}")
# Country with maximum DALYs in 2019: Lesotho; Country with minimum DALYs in 2019: Singapore

country_data=dalys_data.loc[dalys_data["Entity"]==max_country,["Year","DALYs"]]
plt.figure(figsize=(10,5))
plt.plot(country_data["Year"],country_data["DALYs"],'b+', label=max_country)       
plt.title("DALYs over time for " + max_country)
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.xticks(country_data["Year"], rotation=-90)      
plt.legend()
plt.tight_layout()      
plt.show()

# For the one other question asked by myself: Plot a boxplot of DALYs for China and report the range between the maximum and minimum values.
china_dalys = dalys_data.loc[dalys_data["Entity"] == "China", "DALYs"]

plt.figure(figsize=(8, 6))
plt.boxplot(china_dalys)
plt.title("Boxplot of DALYs for China")
plt.ylabel("DALYs")
plt.xticks([1], ["China"])     
plt.tight_layout()
plt.show()

max_dalys = np.max(china_dalys)
min_dalys = np.min(china_dalys)
range_dalys = np.ptp(china_dalys)   

print("Maximum DALYs:", max_dalys)
print("Minimum DALYs:", min_dalys)
print("Range (Maximum - Minimum):", range_dalys)