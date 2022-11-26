import math
x = float(input("x = "))
y = float(input("y = "))
f2 = (1/(x+2/x**2+3/x**3)+math.exp(x**2+3*x))/(math.atan(x+y)+
math.fabs(5+x)*math.fabs(5+x))-math.cos(y*y+x**2/2)*math.cos(y*y+x**2/2)
print(f2)