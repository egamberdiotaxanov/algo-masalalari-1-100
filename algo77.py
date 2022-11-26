import math
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
d = int(input("d = "))
S = float(0)
h = int(2)

for i in range(c,d,2):

    S += math.pow(((math.sin(a*i)+math.pow(b,2*c))/(b*b+math.cos(i)*math.cos(i))),1./3)-\
        math.sin(i*i)/(a*b)
print(round(S,2))