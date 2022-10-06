# 10. Find the distance between two points of space.

import math

print('Enter the coordinates of point a on the x axis: ')
coord_x_point_a = int(input())
print('Enter the coordinates of point b on the x axis:: ')
coord_x_point_b = int(input())
print('Enter the coordinates of point a on the y axis: ')
coord_y_point_a = int(input())
print('Enter the coordinates of point a on the y axis:: ')
coord_y_point_b = int(input())

length_A_B = 0

def Calculate(x_a, x_b, y_a, y_b, length):
    length = math.sqrt((math.pow((x_a - x_b), 2) + math.pow((y_a  - y_b ), 2)))
    print('Answer: ', length)

Calculate(coord_x_point_a, coord_x_point_b,coord_y_point_a,coord_y_point_b, length_A_B)