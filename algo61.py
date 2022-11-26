import math
n = int(input("n = "))
S = 0
for i in range(1,n+1):
    S += math.sin(i)/math.pow(2,i)
print(round(S,2))


"""n = 100

sum = 0
for counter in range(1, n+1):
    sum = sum + counter

print("Sum of 1 until %d: %d" % (n, sum))
Sum of 1 until 100: 5050"""