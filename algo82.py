import math
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
S = float(0)

for i in range(1,10+3,3):
    S += (a*i**2)/b+i/c
print(round(S,2))