import math
n = int(input("n = "))
x = int(input("x = "))
S = float(0)
p = int(1)
for i in range(2,n+1,1):
    p = p * (2 * i - 2)
    S += 1+math.pow(x,2*i-2)/p
print(round(S,3))