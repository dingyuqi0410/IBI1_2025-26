a=5.08
b=5.33
c=5.55
d=b-a
e=c-b
if d>e:
    print("population growth is decelerating in Scotland")
elif d<e:
    print("population growth is accelerating in Scotland")
else:
    print("population growth is not change in Scotland")
#d>e, population growth is decelerating in Scotland
print("\n")
X=True
Y=False
W=X or Y
print("X\tY\tW")
booleans = [True, False]
for X in booleans:
    for Y in booleans:
        W = X or Y
        print( X,"\t",Y,"\t",W)
# Truth table for X,Y,Z:
# | X     | Y     | W     |
# |-------|-------|-------|
# | True  | True  | True  |
# | True  | False | True  |
# | False | True  | True  |
# | False | False | False |