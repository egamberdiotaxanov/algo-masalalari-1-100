import math
a = int(input("a = "))
x = float(input("x = "))
TT = (math.sqrt(x-1)+math.sqrt(x+2)+math.log10(math.sqrt(a*x*x)+2))/\
     (math.sqrt(math.sqrt(x+2)+math.sqrt(x+24)+x**5))
print(round(TT,2))