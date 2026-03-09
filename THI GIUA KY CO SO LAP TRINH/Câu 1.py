a = int(input("nhap so bat ki :"))
b = int(input("nhap so bat ki :"))
c = int(input("nhap so bat ki :"))
if a > b and a > c:
    print("a lon nhat")
elif b > a and b > c:
    print("b lon nhat")
else:
    print("c lon nhat")
if a < b and a < c:
    print("a be nhat")
elif b < a and b < c:
    print("b be nhat")
else:
    print("c be nhat")

import math
a = float(input("nhap so a "))
b = float(input("nhap so b "))
c = float(input("nhap so c "))

d = b*b - 4*a*c

if d > 0:
    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)
    print("x1 =", x1)
    print("x2 =", x2)

elif d == 0:
    x = -b / (2*a)
    print("x =", x)

else:
    print("vo nghiem")