# Write a program that takes the coordinates of a point (X and Y) as input, with X ≠ 0 and Y ≠ 0 and
#  outputs the number of the quarter of the plane in which this point is located (or on which axis it is located).


number_x = int(input('Enter the x coordinate: '))
number_y = int(input('Enter the y coordinate: '))

# Checking the condition


def checking_condition(x, y):
    if x != 0 and y != 0:
        if x > 0 and y > 0:
            print('This point is in 1 quarter')
        if x < 0 and y > 0:
            print('This point is in 2 quarter')
        if x < 0 and y < 0:
            print('This point is in 3 quarter')
        if x > 0 and y < 0:
            print('This point is in 4 quarter')
    else:
        print('Error')


checking_condition(number_x, number_y)
