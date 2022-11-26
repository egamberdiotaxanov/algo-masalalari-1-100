import math
x = int(input("x = "))
y = int(input("y = "))
a = int(input("a = "))
b = int(input("b = "))
S = float(0)
P = float(1)
P1 = float(1)
SP = float(0)
for a in range(1,x+1,1):
    S += (a**2+2*a)/(a**3+a*math.cos(a)**2+1)
print(round(S,2))
for i in range(1,y+1,1):
    P *= (i**2+1)/(math.pow(math.pow(i,3),1./i)+2)
print(round(P,2))
for i in range(1,a+1,1):
    P1 = float(1)
    for k in range(1,b+1,1):
        P1 *= math.log((math.pow(k,i)+math.pow(k,1/i))/(k**3+math.pow(i,1/k)))
    SP += P1
print(round(SP,2))