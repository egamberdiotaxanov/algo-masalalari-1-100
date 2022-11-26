x = int(input("x = "))
y = int(input("y = "))
z = int(input("z = "))
if x>=1 and y>=1 and z>=1:
    print(x**2,y**2,z**2)

elif x>=1 and y<=1 and z<=1:
    print(x**2,y,z)

elif x<=1 and y>=1 and z<=1:
    print(x,y**2,z)

elif x<=1 and y<=1 and z>=1:
    print(x,y,z**2)

elif x<=-1 and y<=-1 and z<=-1:
    print("Sonlarning xammasi manfiy!")