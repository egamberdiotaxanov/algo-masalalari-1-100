import math
a = int(input("a = "))
x = float(input("x = "))
BB1 = x*math.sin(x/2+x/3+x/4)+(math.log10(x*x-2)+3**a)/(math.cos(x+3)*math.sin(x+3)+8)
print(round(BB1,2))