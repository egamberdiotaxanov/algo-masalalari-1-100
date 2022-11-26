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
    S += (a*x+4)/math.sqrt(a+math.log(6))
print(round(S,2))
for a in range(1,y+1,1):
    P *= (a*x**2+6)/math.sin(a*x)
print(round(P,2))
for i in range(1,c+1,1):
    for j in range(1,d+1,1):
        P1 *= (j*i+y*x)/math.sqrt(math.pow((j*x+y),i))
    SP += P1
print(round(SP,2))

# xxx misol