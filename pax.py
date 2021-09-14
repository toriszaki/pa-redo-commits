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
    print(str(point_name) + "x is " + str(points[2][0]) + ", " + str(point_name) +"y is " + str(points[2][1]))
    # print(f"{point_name}y is " + str(points[2][1]))


def calculate_distance(points):
    distance = 0
    for first_coor_to_compare in points[::-1]:
        for second_coor_to_compare in points[::-1]:
            calculating_distance = math.sqrt(math.pow(first_coor_to_compare[1] - second_coor_to_compare[1], 2) + (first_coor_to_compare[0] - second_coor_to_compare[0]) * (first_coor_to_compare[0] - second_coor_to_compare[0]))
            if calculating_distance > distance:
                distance = calculating_distance
                first_endpoint = first_coor_to_compare
                second_endpoint = second_coor_to_compare
    return first_endpoint, second_endpoint, distance


def main():
    print("Welcome to my mystery program!")
    points = []
    get_numbers(points, "A")
    get_numbers(points, "B")
    get_random_numbers(points, "C")
    first_endpoint, second_endpoint, distance = calculate_distance(points)
    print("A " + str(first_endpoint) + ", B" + str(second_endpoint) + ", d:" + str(distance))

main()