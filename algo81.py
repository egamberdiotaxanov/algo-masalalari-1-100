import math
a = int(input("a = "))
b = int(input("b = "))
S = float(0)
for i in range(1,12,2):
    S += a**2+math.pow((b+math.sin(i))/(a**3+math.cos(i**3)*math.cos(i**3)),1./5)
print(round(S,2))