import math
x = float(input("X = "))
y = float(input("y = "))
T11 = (x**2+1)/(x**2+(x*y+y**2)/(y**2+(y+x*y)/(math.fabs(x*y)+5)))+1/(1+math.cos(x)+1/math.sin(math.fabs(x)))
print(T11)