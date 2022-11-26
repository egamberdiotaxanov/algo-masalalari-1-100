import math
n = int(input("n = "))
x = int(input("x = "))
S = float(0)
for i in range(1,2*n,1):

        S += i/math.pow(x,2*i)
print(round(S,3))