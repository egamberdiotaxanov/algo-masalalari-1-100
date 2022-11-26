import math
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
x = float(input("x = "))
W1 = 0.75+(8.2*x*x+math.sqrt(math.fabs(x**3+3*x)+math.cos(x-2)))/(a/4+b/3+c/2+1)
print(round(W1,2))