import math
a = float(input("a = "))
b = float(input("b = "))
T = math.pow(a,1/5)+math.pow(b*(a+b)/(2*b+a*b),1/4)*(a*a+b*b+2)
