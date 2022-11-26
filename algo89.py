import math
import numpy as np
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
S = float(0)
h = float(0.25)
for i in np.arange(0,1+h,h):
    S += math.sqrt((math.sin(a*i)+math.pow(b,c))/(b**2+math.cos(i)**2))-math.sin(i**2)/(a*b)
print(round(S,2))