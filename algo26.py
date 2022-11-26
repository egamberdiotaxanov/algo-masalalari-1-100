import math
a = int(input("a = "))
x = float(input("x = "))
y = float(input("y = "))
e = 2.718
W2 = math.sqrt(math.pow(e,x*y)-x*math.sin(a*x)-(x*x+2)/(math.fabs(x)+5))+math.sqrt(math.log(e,x*x+2)+5)
print(round(W2,2))