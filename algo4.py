"""Radiusi r bo`lgan sharning yuzini toping.
Kiruvchi ma’lumotlar: bitta butun son r (1<=r<=100)
Chiquvchi ma’lumotlar: bitta son masala yechimi. Javobni 10-2 aniqlikdachiqaring.

"""
import math
r = int(input("Sharning radiusini toping:"))
S = 2 * math.pi * r ** 2
print("Sharning yuzi:",S)