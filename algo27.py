import math
x = float(input("x = "))
AA = math.sqrt((2*math.tan(x+2)-math.cos(x+math.pow(2,x)))/
               (1+math.cos(x+2)*math.cos(x+2)))+math.sin(x*x)/(x*x+3)
print(round(AA,2))