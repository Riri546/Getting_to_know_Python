# Write a program that takes the coordinates of a point (X and Y) as input, with X ≠ 0 and Y ≠ 0 and
#  outputs the number of the quarter of the plane in which this point is located (or on which axis it is located).

print('Enter the x coordinate: ')
number_x = int(input())
print('Enter the y coordinate: ')
number_y = int(input())

def checking_condition(x, y):
    if x!=0 and y!=0:
        if x >0 and y >0:
            print('This number is in the first quarter')
        if x <0 and y >0:
            print('This number is in the second quarter')
        if x<0 and y<0:
            print('This number is in the third quarter')
        if x>0 and y<0:
            print('This number is in the fourth quarter')
    else:
        print('Error')

checking_condition(number_x, number_y)


