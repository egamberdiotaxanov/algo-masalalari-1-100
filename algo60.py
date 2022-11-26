import math
x  = float(input("x = "))
y  = float(input("y = "))

y1 = math.sqrt(1-x*x)
if y <= y1 and y <= 0.5 * x + 1 and y >= -0.5 * x - 1:
     print("yes")
else:
     print("no")