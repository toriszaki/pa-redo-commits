import random
import math

def get_numbers(points, point_name):
    x_coordinate = float(input(f"{point_name}x: "))
    print(f"{point_name}x is " + str(x_coordinate))
    y_coordinate = float(input(f"{point_name}y: "))
    print(f"{point_name}y is " + str(y_coordinate))
    points.append((x_coordinate, y_coordinate))


def get_random_numbers(points, point_name):
    points.append((random.random() * 10 - 5, random.random() * 10 - 5))
    print("P3x is " + str(points[2][0]))
    print("P3y is " + str(points[2][1]))



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
    points = []
    get_numbers(points, point_name)
    get_random_numbers(points, point_name)
    a, b, x = calculate_distance(points)
    print("A " + str(a) + ", B" + str(b) + ", d:" + str(x) )