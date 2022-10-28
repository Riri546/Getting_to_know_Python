# 5. Find the distance between two points of space.

import math

coord_x_point_a = int(input('Enter the coordinates of point a on the x axis: '))
coord_x_point_b = int(input('Enter the coordinates of point b on the x axis: '))
coord_y_point_a = int(input('Enter the coordinates of point a on the y axis: '))
coord_y_point_b = int(input('Enter the coordinates of point a on the y axis: '))


def Calculate(x_a, x_b, y_a, y_b, length):
    length = math.sqrt((math.pow((x_a - x_b), 2) + math.pow((y_a - y_b), 2)))
    print(f'Answer: {length}')


Calculate(coord_x_point_a, coord_x_point_b,
          coord_y_point_a, coord_y_point_b, 0)
