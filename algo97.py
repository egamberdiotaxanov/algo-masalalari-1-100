import math
x = int(input("x = "))
y = int(input("y = "))
c = int(input("c = "))
d = int(input("d = "))
S = float(0)
SP = float(0)
P = float(1)
P1 = float(1)
for n in range(1,x+1,1):
    S += 1/(5-17*n+n**3)
print(round(S,2))
for m in range(1,y+1,1):
    P *= math.sqrt(math.fabs(m-5)+1)/(m**2+4*m+math.pow(-1,3.))
print(round(P,2))
for i in range(1,c+1,1):
    for k in range(1,d+1,1):
        P1 *= math.pow(-1,i)*math.pow(math.fabs(math.sin(k)+math.exp(k)),1./7)/(2*math.fabs(4*i**3-k**4))
    SP += P1
print(round(SP,2))