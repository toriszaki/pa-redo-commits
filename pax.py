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
    print(f"{point_name}x is " + str(points[2][0]))
    print(f"{point_name}y is " + str(points[2][1]))


def calculate_distance(points):
    distance = 0
    a = points[0]
    b = points[1]
    for p in points[::-1]:
        for q in points[::-1]:
            if math.sqrt((p[0] - q[0]) * (p[0] - q[0]) + math.pow(p[1] - q[1], 2)) > distance:
                distance = math.sqrt(math.pow(p[1] - q[1], 2) + (p[0] - q[0]) * (p[0] - q[0]))
                a = p
                b = q
    return a, b, distance


def main():
    print("Welcome to my mystery program!")
    points = []
    get_numbers(points, "A")
    get_numbers(points, "B")
    get_random_numbers(points, "C")
    a, b, x = calculate_distance(points)
    print("A " + str(a) + ", B" + str(b) + ", d:" + str(x) )

main()