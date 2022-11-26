import math
n = int(input("n = "))
x = int(input("x = "))
S = float(0)
p = int(1)
for i in range(1,n+2,2):
    S += math.pow(x,i)/i

print(round(S,3))