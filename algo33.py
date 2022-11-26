x = int(input("x = "))
y = int(input("y = "))
z = int(input("z = "))
m0 = x+y+z
n0 = x+y/2
mx = max(m0,x,y,z)
mn = min(n0,x,y,z)**2
print("Max:",mx,"Min:",mn)