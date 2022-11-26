import math
n = int(input("n = "))
S = 0
for i in range(1,n+1):
    S += math.pow((-1),i-1)*math.sin(math.pow(i,i))/math.pow(2,i)
print(round(S,2))