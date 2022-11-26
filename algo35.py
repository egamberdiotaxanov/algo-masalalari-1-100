import math
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
if a>=b>=c:
    print(a*2,b*2,c*2)
else:
    a0 = math.fabs(a)
    b0 = math.fabs(b)
    c0 = math.fabs(c)
    print(a0,b0,c0)