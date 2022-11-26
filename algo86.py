import math
import numpy as np
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
S = float(0)
h = float(0.25)
for i in np.arange(c,b+h,h):
    S += a**2*math.cos(i)+math.sin(i)/2+b*i**2
print(round(S,2))