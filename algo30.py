import math
x = int(input("x = "))
y = float(input("y = "))
z = float(input("z = "))
e = 2.718
AF = math.pow(2,-x)*math.sqrt(x+math.pow(math.fabs(y)+2,1/4))*math.pow(math.pow(e,x-1)/math.sin(z+2)+2,1/3)
print(round(AF,2))