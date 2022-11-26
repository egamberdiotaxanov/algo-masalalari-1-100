"""Radiuslari r1, r2, r3 bo’lgan 3 to doira radiuslari berilgan. Doiralarni yuzlarinihisoblang.
Kiruvchi ma’lumotlar: uchta butun son r1,r2,r3 (1<=r1,r2,r3<=100)
Chiquvchi ma’lumotlar: uchta son doiralar yuzlari javoblarni 10-2 aniqlikdachiqaring.
"""
import math
r1 = int(input("Birinchi doira radiusini kiriting:"))
r2 = int(input("Ikkinchi doiraning yuzini kiriting:"))
r3 = int(input("Uchinchi doiraning yuzini kiriting:"))
s1 = math.pi * r1 ** 2
s2 = math.pi * r2 ** 2
s3 = math.pi * r3 ** 2
print("Birinchi doira yuzi:",s1)
print("Ikkinchi doira yuai:",s2)
print("Uchinchi doira yuzi:",s3)