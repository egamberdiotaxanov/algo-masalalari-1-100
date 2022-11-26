import math
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
S = float(0)
h = int(2)
for i in range(a,b,h):

    S = S + (math.pow(a,b)+math.pow(b,i)+math.pow(c,a))*1./(2*i*i+3*math.pow(a,i))
print(round(S,2))