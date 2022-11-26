import math
x  = float(input("x = "))
y  = float(input("y = "))

S = (math.pi*1*360)/180

if y<=math.sqrt(1-x**2):
    print("yes")
else:
    print("no")