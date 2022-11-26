x = float(input("x = "))
y = float(input("y = "))
z = float(input("z = "))
if x<1 and y<1 and z<1:
    if x>y:
        if y>z:
            z = (x+y)/2
            print(x,y,z)
        else:
            y = (x+z)/2
            print(x,y,z)
    else:
        x = (y+z)/2
        print(x,y,z)
else:
    print(x,y,z)