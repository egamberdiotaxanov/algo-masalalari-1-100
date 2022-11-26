import math
import numpy as np
a = int (input("a = "))
S = float(0)
for i in np.arange(0,10+0.5,0.5):
    S += a * math.cos(i) - math.sin(i**2)
print(round(S,2))