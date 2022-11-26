import math
x  = float(input("x = "))
y  = float(input("y = "))

if y<=math.sqrt(1-x**2) and y<=x/2:
    print("yes")
else:print("no")