import math
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
d = int(input("d = "))
S = float(0)
P = float(1)
for m in range(1,a+1,1):
    S += (3*m**3+4*m+5)/(m**3+math.log(m))
print(round(S,2))
for k in range(1,b+1,1):
    P *= k/(k**3+7*k+5)
print(round(P,2))
SP = float(0)
for i in range(1,c+1,1):
    P1 = float(1)
    for m in range(1,d+1,1):
        P1 *= (math.log2(i)+math.pow(m,i))/math.pow(m,i)
    SP += P1
print(round(SP,2))