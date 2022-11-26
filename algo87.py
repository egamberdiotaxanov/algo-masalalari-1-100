import math
import numpy as np
a = int(input("a = "))
S = float(0)
n = float(math.pi/10.)
for i in np.arange(-math.pi/2.,math.pi+n,n):
    S += 2*math.pow(a,math.sin(2*i))+i**2*math.cos(a*i)
print(round(S,2))