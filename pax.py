import math

print("Welcome to my mystery program!")

a=float(input("P1x: "))
print("P1x is " + str(a))
b=float(input("P1y: "))
print("P1y is " + str(b))
c=float(input("P2x: "))
print("P2x is " + str(c))
d=float(input("P2y: "))
print("P2y is " + str(d))
import random
import math
pts = []

pts.append((a,b))
pts.append((c,d))
pts.append((random.random() * 10 - 5, random.random() * 10 - 5))
print("P3x is " + str(pts[2][0]))
print("P3y is " + str(pts[2][1]))

x = 0
a = pts[0]
b = pts[1]
for p in pts[::-1]:
    for q in pts[::-1]:
        if math.sqrt((p[0] - q[0]) * (p[0] - q[0]) + math.pow(p[1] - q[1], 2)) > x:
            x = math.sqrt(math.pow(p[1] - q[1], 2) + (p[0] - q[0]) * (p[0] - q[0]))
            a = p
            b = q

print("A " + str(a) + ", B" + str(b) + ", d:" + str(x) )

