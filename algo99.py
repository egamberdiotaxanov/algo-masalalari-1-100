import math
x = int(input("x = "))
y = int(input("y = "))
c = int(input("c = "))
d = int(input("d = "))
S = float(0)
SP = float(0)
P = float(1)
P1 = float(1)
for k in range(1,x+1,1):
    S += k**3+math.exp(k)
print(round(S,2))
for a in range(3,y+1,1):
    P *= (a*x)/(math.sqrt(a**2+x**2))
print(round(P,2))
for i in range(1,c+1,1):
    for j in range(1,d+1,1):
        P1 *= (i*x+j**2)/(math.sqrt(i**2+j*y))
    SP += P1
print(round(SP,2))

# xxx misol