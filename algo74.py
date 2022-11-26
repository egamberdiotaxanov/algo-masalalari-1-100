import math
n = int(input("n = "))
x = int(input("x = "))
S = float(0)
p = int(1)
for i in range(1,n+1,1):
    m = 2*i-1
    for j in range(1,m+1,1):
        p = p * j
    S += math.pow(x,2*i-1)/p
print(round(S,3))