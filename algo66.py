import math
n = int(input("n = "))
x = int(input("x = "))
S = float(0)
for i in range(1,n+1,1):
    S += math.pow(-1,i-1) * (1/i) * math.sin(i*x)
print(round(S,3))