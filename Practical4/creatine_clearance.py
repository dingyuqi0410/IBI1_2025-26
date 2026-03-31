# first stores the value of age, weight, gender and Cr
# use if-statement and elif to test whether the input values are correct, if no, print which one
# use else to express when the values are correct, begin calculation
# use if and else to test the gender (male/female), calculate respectively
#print the final result
age=19
weight=55
gender="female"
Cr=1.2
if age>=100:
    print("Age needs corrected!")
elif weight<=20 or weight>=80:
    print("Weight needs corrected!")
elif Cr<=0 or Cr>=100:
    print("Cr needs corrected!")
elif gender!="female" and gender!= "male":
    print("Gender needs corrected!")
else:    
    if gender=="male":   
        CrCl = (140 - age) * weight / (72 * Cr)
    else:
        CrCl = (140 - age) * weight / (72 * Cr) * 0.85 
    print(str(CrCl))   