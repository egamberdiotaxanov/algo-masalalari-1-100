import math
x = float(input("x = "))
y = float(input("y = "))
c1 = (x+y)/(y**2+math.fabs((y**2+2)/(x+x**3/5)))+math.exp(y+2)
print(c1)