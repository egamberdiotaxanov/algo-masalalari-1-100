import math
x = float(input("x = "))
y = float(input("y = "))
f1 = (2*math.tan(x+math.pi/6))/(1/3+math.cos(y+x**2)*math.cos(y+x**2))+math.log2(x**2+2)
print(f1)