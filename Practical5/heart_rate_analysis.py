import matplotlib.pyplot as plt
#step 1
heart_rates=[72,60,126,85,90,59,76,131,88,121,64]
patients_number=len(heart_rates)   
mean_heart_rate=sum(heart_rates)/patients_number       #求和用sum()
print(f"There are {patients_number} patients are in the dataset. And the mean heart rate is {mean_heart_rate}.")
#step 2
low_count=0   #这一步非常关键，计数时必须要先设置初始值
high_count=0
normal_count=0
for heart_rate in heart_rates:
    if heart_rate<60:
        low_count+=1      #采用计数的方法
    elif heart_rate>120:
        high_count+=1
    else:
        normal_count+=1
print(f"Low: {low_count}")
print(f"Normal: {normal_count}")
print(f"High: {high_count}")
categories={"Low": low_count,"Normal": normal_count, "High": high_count}                   
print(f"The largest category is: {max(categories,key=categories.get)}")     #重要：max(categories,key=categories.get)的意思是：在categorie这个字典里，找出对应值最大的那个键；max会默认比较key，所以令key=categories.get，相当于key是一个比较规则和标准；categories.get是一个查字典里对应值的工具
#step 3
labels=f"Low: {low_count} patients",f"Normal: {normal_count} patients",f"High: {high_count} patients"     #直接把人数写在label里面
sizes=list(categories.values())
plt.pie(sizes,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90)
plt.title("Distribution of Heart Rate Categories")
plt.axis('equal')
plt.show()