import math
n = int(input("n = "))
x = int(input("x = "))
S = float(0)
p = int(1)
for i in range(1,n+1,1):
    m = 2*i-2
    for j in range(1,m+1,1):
        p *= j
    S += math.pow(-1,i-1)*math.pow(x,2*i-2)/p

print(round(S,3))