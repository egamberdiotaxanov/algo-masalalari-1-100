import math
n = int(input("n = "))
k = int(input("k = "))
S = float(0)
p = int(1)
for i in range(1,n+1,1):
    p = p * i
    S += math.pow(-1,i-1)*math.pow(k,i)/p
print(round(S,3))