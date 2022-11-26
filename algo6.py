"""Asoslari a va b, balandligi h bo`lgan g`ola yuzini toping.
Kiruvchi ma’lumotlar: uchta butun son a,b,h (1<=a,b,h<=100)
Chiquvchi ma’lumotlar: bitta son masala yechimi. Javobni 10-2 aniqlikda chiqaring.
Kiruvchi ma’lumotlar	Chiquvchi ma’lumotlar
8 2 9	>>>202.43
17 11 3	>>>508.61

"""
import math
a = int(input("a = "))
b = int(input("b = "))
h = int(input("h = "))

R = a / 2
r = b / 2
l = math.sqrt(h*h+(R-r)*(R-r))
S = math.pi*(R*R+r*r+l*(R+r))
print("S = ",S)