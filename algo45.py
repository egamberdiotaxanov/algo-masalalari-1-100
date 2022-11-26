import math
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
D:float = b*b-4*a*c
if D > 0:
    x1 = (-b+math.sqrt(D))/(2*a)
    x2 = (-b-math.sqrt(D))/(2*a)
    print(round(x1,2),round(x2,2))

else:
    print("No")