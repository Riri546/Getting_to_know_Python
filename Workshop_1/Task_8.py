# 8. Tell in which quarter of the coordinate plane or on which
# axis is the point with the X and Y coordinates.
print('Enter the x coordinate: ')
number_x = int(input())
print('Enter the y coordinate: ')
number_y = int(input())


def checking_condition(x, y):
    if x > 0 and y > 0:
        print('This point is in 1 quarter')
    if x < 0 and y > 0:
        print('This point is in 2 quarter')
    if x < 0 and y < 0:
        print('This point is in 3 quarter')
    if x > 0 and y < 0:
        print('This point is in 4 quarter')
    if x > 0 or x < 0 and y == 0:
        print('This point is located on the abscissa axis')
    if y > 0 or y < 0 and x == 0:
        print('This point is located on the ordinate axis')


checking_condition(number_x, number_y)
