import math
x = float(input("x = "))
y = float(input("y = "))
if x<=-1 and y<=-1:
    x = math.fabs(x)
    y = math.fabs(y)
    print(x,y)
if x<=-1 or y<=-1:
        x = x + 0.5
        y = y + 0.5
        print(x,y)
else: print(x,y)