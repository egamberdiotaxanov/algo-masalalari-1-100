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
    S += (math.pow(-1,k)*(k+1))/(k**3+k**2+1)
print(round(S,2))
for i in range(1,y+1,1):
    P *= (i**3+math.fabs(i-9))/(math.log2(i)+7*i)
print(round(P,2))
for n in range(1,c+1,1):
    for m in range(1,d+1,1):
        P1 *= math.pow(-1,m)*math.log(m+5)/(math.pow(m,(n+5))+n*m)
    SP += P1
print(round(SP,2))