# give the initial students number, the rate, the total students number, and the initial days
# print the day and the inflected students number at the beginning
# use while-loop to compare inflected and the total
# while inflected < total number, calculate the inflected number and the day now
# print the day and the inflected students number 
# until inflected > total number, quit while cycle
# print the day number
inflected=5  
rate=0.4
total=91
days=1
print(f"day: {days}, inflected students:{inflected}")
while inflected < total:   
    inflected=inflected*(1+rate)     
    days+=1   #remember to +1 of the days
    print(f"day: {days}, inflected students:{inflected}")
print(days)