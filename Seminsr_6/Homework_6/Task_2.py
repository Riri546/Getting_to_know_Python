# 10. Find the distance between two points of space.


import math


x_a = int(input('Enter the coordinates of point a on the x axis: '))
x_b = int(input('Enter the coordinates of point b on the x axis: '))
y_a = int(input('Enter the coordinates of point a on the y axis: '))
y_b = int(input('Enter the coordinates of point a on the y axis: '))


length = lambda a_x, a_y, b_x, b_y: math.sqrt((math.pow((a_x - b_x), 2) + math.pow((a_y - b_y), 2)))
print(length(x_a, x_b, y_a, y_b))


# def Calculate(x_a, x_b, y_a, y_b, length):
#     length = math.sqrt((math.pow((x_a - x_b), 2) + math.pow((y_a - y_b), 2)))
#     print(f'Answer: {length}')


# Calculate(coord_x_point_a, coord_x_point_b,
#           coord_y_point_a, coord_y_point_b,0)


