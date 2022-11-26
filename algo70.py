import math
n = int(input("n = "))
x = int(input("x = "))
S = float(0)
p = int(1)
for i in range(1,n+1,1):

    S = S+math.pow(-1,i)*(math.pow(x,2*i-1)/p)
    p = p * (i+2)

print(round(S,3))