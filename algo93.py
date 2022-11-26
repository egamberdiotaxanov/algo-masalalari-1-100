import math
x = int(input("x = "))
y = int(input("y = "))
a = int(int(input("a = ")))
b = int(input("b = "))
S = float(0)
P = float(1)
P1 = float(1)
SP = float(0)
for k in range(1,x+1,1):
    S += (k**2*math.sin(k)+5)/math.pow((k**7+1),1./5)
print(round(S,2))
for n in range(1,y+1,1):
    P *= (n+math.sqrt(n))/(n-math.pow((n+1),1./5))
print(round(P,2))
for k in range(1,a+1,1):
    for i in range(1,b+1,1):
        P1 *= (i**2+math.pow(k**2,1./i))/((math.sin(i)+math.cos(k))*math.pow(i,k))
    SP += P1
print(round(SP,2))