import random
import math

def get_numbers(points, point_name):
    coordinate = []
    axis = ["x", "y"]
    for index in range(len(axis)):
        coordinate.append(float(input(f"{point_name}{axis[index]}: ")))
        print(f"{point_name}{index} is " + str(coordinate[index]))
    coordinates = (coordinate[0], coordinate[1])
    points.append(coordinates)


def get_random_numbers(points, point_name):
    points.append((random.random() * 10 - 5, random.random() * 10 - 5))
    print(f"{point_name}x is " + str(points[2][0]))
    print(f"{point_name}y is " + str(points[2][1]))


def calculate_distance(points):
    distance = 0
    for first_coor_to_compare in points[::-1]:
        for q in points[::-1]:
            calculating_distance = math.sqrt(math.pow(first_coor_to_compare[1] - q[1], 2) + (first_coor_to_compare[0] - q[0]) * (first_coor_to_compare[0] - q[0]))
            if calculating_distance > distance:
                distance = math.sqrt(math.pow(first_coor_to_compare[1] - q[1], 2) + (first_coor_to_compare[0] - q[0]) * (first_coor_to_compare[0] - q[0]))
                a = first_coor_to_compare
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