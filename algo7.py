"""          Ko`nusni balandligi h va radiusi r bo`lsa uni hajmi nimaga teng bo`ladi.
Kiruvchi ma’lumotlar: ikkita butun son h,r (1<=h,r<=100)
Chiquvchi ma’lumotlar: bitta son masala yechimi. Javobni 10-2 aniqlikda chiqaring.
Kiruvchi ma’lumotlar	Chiquvchi ma’lumotlar
3 5	    >>>78.54
19 6	>>>716.28

"""
import math
h = int(input("h = "))
r = int(input("r = "))
x = math.pi*h*r*r/3
print(x)