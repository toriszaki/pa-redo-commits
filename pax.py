import random
import math

def get_numbers():
    a1_coordinate=float(input("Ax: "))
    print("Ax is " + str(a1_coordinate))
    a2_coordinate=float(input("Ay: "))
    print("Ay is " + str(a2_coordinate))
    c=float(input("P2x: "))
    print("P2x is " + str(c))
    d=float(input("P2y: "))
    print("P2y is " + str(d))
    points = []
    points.append((a1_coordinate, a2_coordinate))
    points.append((c,d))
    points.append((random.random() * 10 - 5, random.random() * 10 - 5))
    print("P3x is " + str(points[2][0]))
    print("P3y is " + str(points[2][1]))
    return points


def calculate_distance():
    x = 0
    a = pts[0]
    b = pts[1]
    for p in pts[::-1]:
        for q in pts[::-1]:
            if math.sqrt((p[0] - q[0]) * (p[0] - q[0]) + math.pow(p[1] - q[1], 2)) > x:
                x = math.sqrt(math.pow(p[1] - q[1], 2) + (p[0] - q[0]) * (p[0] - q[0]))
                a = p
                b = q
    return a, b, x


def main():
    print("Welcome to my mystery program!")
    points = get_numbers()
    a, b, x = calculate_distance(points)
    print("A " + str(a) + ", B" + str(b) + ", d:" + str(x) )