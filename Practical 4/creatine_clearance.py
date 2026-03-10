# first stores the value of age, weight, gender and Cr
age=19
weight=55
gender="female"
Cr=1.2
# use first if-statement to test whether the input values are correct, if no, print which one
if age>=100:
    print("Age needs corrected!")
elif weight<=20 or weight>=80:
    print("Weight needs corrected!")
elif Cr<=0 or Cr>=100:
    print("Cr needs corrected!")
elif gender!="female" and gender!= "male":
    print("Gender needs corrected!")
else:    #if the values are correct, begin calculation
    #test the gender (male/female), calculate respectively
    if gender=="male":   
        CrCl = (140 - age) * weight / (72 * Cr)
    else:
        CrCl = (140 - age) * weight / (72 * Cr) * 0.85 
    print(str(CrCl))   #print the final result
