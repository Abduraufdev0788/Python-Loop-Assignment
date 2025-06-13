num = int(input("sonni kiritiing: "))
n = 0

while num != 0 :
    n += num % 10
    num //= 10
print(n)
