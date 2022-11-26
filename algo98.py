import math
x = int(input("x = "))
y = int(input("y = "))
c = int(input("c = "))
d = int(input("d = "))
S = float(0)
SP = float(0)
P = float(1)
P1 = float(1)
for a in range(1,x+1,1):
    S += (4*a+6*math.log(a))/(a**2+a)
print(round(S,2))
for a in range(1,y+1,1):
    P *= math.fabs(a-6*math.cos(a))/(a**2+math.pow(a,math.log(a)))
print(round(P,2))
for k in range(1,c+1,1):
    for a in range(1,d+1,1):
        P1 *= (a*k+x)/(k**2+y**2)
    SP += P1
print(round(SP,2))