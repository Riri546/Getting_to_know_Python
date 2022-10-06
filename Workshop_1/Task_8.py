# 8. Tell in which quarter of the coordinate plane or on which
# axis is the point with the X and Y coordinates.
print('Enter the x coordinate: ')
number_x = int(input())
print('Enter the y coordinate: ')
number_y = int(input())


def checking_condition(x, y):
    if x != 0 and y != 0:
        if x > 0 and y > 0:
            print('This number is in the first quarter')
        if x < 0 and y > 0:
            print('This number is in the second quarter')
        if x < 0 and y < 0:
            print('This number is in the third quarter')
        if x > 0 and y < 0:
            print('This number is in the fourth quarter')
    else:
        print('Error')


checking_condition(number_x, number_y)
