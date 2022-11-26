import math
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
S = float(0)
h = int(3)
for i in range(a,c+h,h):

    S += math.pow(((a*i*1.+b)/(b*b+math.cos(i*1.)*math.cos(i*1.))),1./3)-\
         math.sin(i*i*1.)/(a*b*1.)

print(round(S,2))