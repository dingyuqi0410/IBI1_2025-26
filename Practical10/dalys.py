import os      #用于处理文件和目录
import pandas as pd       #用于处理dataframe
import matplotlib.pyplot as plt
import numpy as np

os.chdir("/Users/a18274964300/Documents/大一下/IBI1/IBI1_2025-26/IBI1_2025-26/Practical10")    #把当前工作目录改成存放csv文件的目录
print(os.getcwd())
print(os.listdir())

dalys_data=pd.read_csv("dalys-rate-from-all-causes.csv")

first_10_year_dalys=dalys_data.iloc[0:10,2:4]     #0:10代表前10行，2:4代表编号第2～3列（也就是第3～4列）
print(first_10_year_dalys)
max_dalys_first_10=first_10_year_dalys["DALYs"].max()     #找到"DALYs"列的最大值
max_year_first_10=first_10_year_dalys.loc[first_10_year_dalys["DALYs"]==max_dalys_first_10,"Year"].iloc[0]     #数据.loc[筛选哪些行，筛选哪些列]，加一个.iloc[0]就可以只print数字,不加的话得到的输出结果会是“8    1998”    
print(f"Year with maximum DALYs in the first 10 Afghanistan rows: {max_year_first_10}")     
# The year with the maximum DALYs across the first 10 recorded years for Afghanistan is: 1998

zimbabwe_rows=dalys_data["Entity"]=="Zimbabwe"     #结果会是一个由 True 和 False 组成的 Boolean 序列，是->True，不是->False
zimbabwe_years=dalys_data.loc[zimbabwe_rows,"Year"]      #只保留 Zimbabwe 的那些行，再只取 Year 这一列
print(zimbabwe_years)
first_zimbabwe_year=zimbabwe_years.min()
last_zimbabwe_year=zimbabwe_years.max()
print(f"First Zimbabwe year: {first_zimbabwe_year}")
print(f"Last Zimbabwe year: {last_zimbabwe_year}")
# The first year recorded: 1990
# The last year recorded: 2019

recent_data=dalys_data.loc[dalys_data.Year==2019,["Entity","DALYs"]]
max_country=recent_data.loc[recent_data["DALYs"]==recent_data["DALYs"].max(),"Entity"].iloc[0]
print(f"Country with maximum DALYs in 2019: {max_country}")
min_country=recent_data.loc[recent_data["DALYs"]==recent_data["DALYs"].min(),"Entity"].iloc[0]
print(f"Country with minimum DALYs in 2019: {min_country}")
# Country with maximum DALYs in 2019: Lesotho
# Country with minimum DALYs in 2019: Singapore

country_data=dalys_data.loc[dalys_data["Entity"]==max_country,["Year","DALYs"]]
plt.figure(figsize=(10,5))
plt.plot(country_data["Year"],country_data["DALYs"],'b+')       #"b+"代表蓝色加号标记,画图用蓝色加号标记表示每一个数据点
plt.title("DALYs over time for " + max_country)
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.xticks(country_data["Year"], rotation=-90)      #把 x 轴每一个年份都显示出来，并把标签旋转 -90 度，避免重叠
plt.tight_layout()      #自动调整图的布局，防止标题和坐标轴文字挤在一起
plt.show()

# For the one other question asked by myself
china_dalys = dalys_data.loc[dalys_data["Entity"] == "China", "DALYs"]

plt.figure(figsize=(8, 6))
plt.boxplot(china_dalys)
plt.title("Boxplot of DALYs for China")
plt.ylabel("DALYs")
plt.xticks([1], ["China"])      #在x轴的第1个位置上,显示标签 "China"
plt.tight_layout()
plt.show()

max_dalys = china_dalys.max()
min_dalys = china_dalys.min()
range_dalys = max_dalys - min_dalys

print("Maximum DALYs:", max_dalys)
print("Minimum DALYs:", min_dalys)
print("Range (Maximum - Minimum):", range_dalys)