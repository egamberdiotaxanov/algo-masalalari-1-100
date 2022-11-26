import math
import numpy as np
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
S = float(0)
h = float(math.pi/10.)

for i in np.arange(-math.pi,math.pi+h,h):

    S += (math.log(math.pow(a,2*math.sin(i)))+math.exp(2*i))/(math.atan(i)+b)+c
print(round(S,2))