import math
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
S = float(0)
for i in range(1,20,5):
    S += (a*i**2+b*i+c)/(a**2+b**2+i**2)
print(round(S,2))