a = float(input("a = "))
if a < -1:
    y = -1/a**2
    print(round(y,2))
elif a < 2:
        y = a**2
        print(round(y,2))
else:
        y = a
        print(round(y,2))
