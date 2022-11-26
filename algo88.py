import math
import numpy as np
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
d = int(input("d = "))
S = float(0)
h = float(1.5)
for i in np.arange(d,c,h):
    S += math.pow((a*i+b)/(b**2+math.cos(i)**2),1./5)-math.sin(i**2)/(a*b)
print(round(S,2))