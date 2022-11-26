x = int(input("x = "))
y = int(input("y = "))
if x!=y:
    if x<y:
        print((x+y)/2,y*x*4)
    else:
        print(x*y*4,(x+y)/2)
else:
    print("Ikkala sonlar teng!")