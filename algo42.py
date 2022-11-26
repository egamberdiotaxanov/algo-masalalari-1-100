a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
d = float(input("d = "))
mn = min(a,b,c,d)
if a<=b and b<=c and c<=d:
    if a<b:
        if b<c:
            if c<d:
                print(d,d,d,d)
            else: print(c,c,c,c)
        else: print(b,b,b,b)
    else: print(a,a,a,a)
else: print(mn,mn,mn,mn)