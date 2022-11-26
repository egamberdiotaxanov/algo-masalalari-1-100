import math
n = int(input("n = "))
x = int(input("x = "))
S = float(0)
for i in range(1,n+1,1):
    S += math.pow(x,i)/math.sqrt(i)
print(round(S,3))