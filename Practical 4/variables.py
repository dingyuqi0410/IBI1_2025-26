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
X=True
Y=False
W=X or Y
print(W)
# the truth table for W: W = True