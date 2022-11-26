import math
x1 = float(input("x1 = "))
x2 = float(input("x2 = "))
c = int(input("c = "))
d = int(input("d = "))
F = math.fabs(math.sin(c*x2**3+d*x1**3-c*d)/math.sqrt((c*x1**2+d*x2**2+5)+2))+math.tan(x1*x2**2+d**3)
print(round(F,2)) #round(F,2) bu 10 usti -2 aniqlikda chiqaradi javobni