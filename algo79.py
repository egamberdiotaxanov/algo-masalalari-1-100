import math
import numpy as np
a = int(input("a = "))
S = float(0)
pi = float(math.cos(-1))
h = float(pi/19.)
a0 = float(-pi/2.)

for i in np.arange(-math.cos(-1)/2,math.cos(-1)+math.cos(-1)/19,math.cos(-1)/19):      #np.arange (start, stop, step)

    S += math.pow(math.pow(a,a),1/3)+(i*i)*math.cos(a*i)

print(round(S,2))