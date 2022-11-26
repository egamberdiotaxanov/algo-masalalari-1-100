a = float(input("a = "))
if a < 0:
    y = -a
    print(y)
elif a < 1:
    y = a
    print(y)
elif a < 2:
    y = 1
    print(y)
else:
    y = 1 - (a - 2) * 2
    print(round(y,2))
