# give the initial students number, the rate, the total students number, and the initial days
inflected=5  
rate=0.4
total=91
days=1
print(f"day: {days}, inflected students:{inflected}")
# use while-loop to compare inflected and the total
while inflected < total:   
    inflected=inflected*(1+rate)     #calculate the inflected number now
    days+=1   #remember to +1 of the days
    print(f"day: {days}, inflected students:{inflected}")
print(days)