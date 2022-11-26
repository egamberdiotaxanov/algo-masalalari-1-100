import math
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
d = int(input("d = "))
x = float(input("x = "))
y2 = (a*x*x+b*x+c)/(x*a**3+a*a+math.pow(a,b-c))+math.cos(math.fabs((a*x+b)/(c*x+d+math.pow(2,c))))
print(round(y2,2))