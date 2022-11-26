import math
n = int(input("n = "))
S = float(0)

for i in range(1,n+1,1):
    P = float(1)
    for j in range(1,(2*i-1)+1,1):
        P *= j
    S += math.pow(-1,i-1)*(1/P)
print(round(S,4))