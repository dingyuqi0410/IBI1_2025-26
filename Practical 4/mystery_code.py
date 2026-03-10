# What does this piece of code do?
# Answer:generate 11 integers between 1 and 10 randomly, add them, and print the total of them

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

total_rand = 0     #give initial= 0
progress=0      #the count=0, it is used to count the times of the loop
while progress<=10:   #when progress<=10, the loop will continue. if progress arrive 11, the while-loop will stop
	progress+=1     #each time the loop runs, progress increased by 1
	n = randint(1,10)    #let the variable n = the random number between 1 and 10
	total_rand+=n      #add n

print(total_rand)   #print the total result

