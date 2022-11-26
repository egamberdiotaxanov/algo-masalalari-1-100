a = float(input("a = "))

if a < -1:
    y = -a - 1
    print(round(y,2))
elif a < 0:
    y = a + 1
    print(round(y, 2))
elif a < 1:
    y = 1 - a
    print(round(y, 2))
else:
    y = a - 1
    print(round(y, 2))
