# give the initial students number, the rate, the total students number, and the initial days
# use while-loop to compare current_infected and the total
# while current_infected < total number, calculate the infected number and the day now
# print the day and the infected students number 
# until current_infected > total number, quit while cycle
# print the day number
initial_infected=5  
rate=0.4
total=91

current_infected=initial_infected
days=0

print("Day\tInfected Students")
print("------------------------")

while current_infected < total: 
    days+=1   #remember to +1 of the days  
    current_infected=current_infected*(1+rate)     
    if current_infected > total:
        current_infected = total
    print(f"{days}\t{current_infected:.1f}")
print(f"Total days to infect all {total} students: {days} days")