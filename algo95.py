import math
x = int(input("x = "))
y = int(input("y = "))
c = int(input("c = "))
d = int(input("d = "))
S = float(0)
SP = float(0)
P = float(1)
P1 = float(1)
for i in range(1,x+1,1):
    S += (i**4+i**2+3)/math.sqrt(i+math.exp(i))
print(round(S,2))
for k in range(1,y+1,1):
    P *= (k+1)/(k**3+5*k)
print(round(P,2))
for m in range(1,c+1,1):
    for n in range(1,d+1,1):
        P1 *= math.sqrt(math.fabs(math.pow(m,n)-math.pow(n,m))/(math.pow(m,n)+math.pow(n,m)))
    SP += P1
print(round(SP,2))

# xxx_misol