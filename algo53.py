import math
x  = float(input("x = "))
y  = float(input("y = "))

if y <= 1.5 and y >= x and y >= -x and y <= 0:
    print("yes")
elif y <= 1.5 and y >= x and y >= -x and y >= 0:
    print("yes1")
else:
    print("no")