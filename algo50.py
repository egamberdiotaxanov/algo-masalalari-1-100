x = float (input("x = "))
y = float(input("y = "))
x1 = 2 + 3 * x
x2 = 2 - 3 * x
if x >= x1 and x <= x2 and y <= 2 and y >= -1:
    print("yes")
else:
    print("no")