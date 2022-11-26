import math
n = int(input("n = "))
x = int(input("x = "))
S = float(0)
p = int(1)
for i in range(1,n+1,1):
    S = S + math.pow(x,i)/p
    p = p * (i+1)
print(round(S,3))
