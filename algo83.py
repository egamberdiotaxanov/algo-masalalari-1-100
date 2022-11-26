import math
import numpy as np
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
S = float(0)
h = float(0.5)
for i in np.arange(5,10+h,h):
    S += (a**2+b*i+math.pow(i,c))/(a**2+b**2+i**2)
print(round(S,2))