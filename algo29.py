import math
a = int(input("a = "))
x = float(input("x = "))
y = float(input("y = "))
e = 2.718
TT = math.sqrt(y*y+math.pow(e,x)+math.sqrt(math.pow(e,x)+a/(x*x+2))+math.cos(x)*math.cos(x)/
               math.sin(x*x))+math.cos(x)**3
print(round(TT,2))