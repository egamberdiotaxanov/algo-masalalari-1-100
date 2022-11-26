import math
x = float(input("x = "))
y = float(input("y = "))
y1 = math.fabs(x)
if y < y1 and y >= -2 and x >= -1 and x <= 1:
    print("yes")
else: print("no")