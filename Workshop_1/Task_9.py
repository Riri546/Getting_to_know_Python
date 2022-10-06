# 9. By specifying the number of the quarter of the rectangular coordinate system, show
# the acceptable coordinate values for the points of this quarter

print('Enter the quarter number: ')
number = int(input())

# The method determines the ranges x and h by the number of the quarter
def print_answer(num):
    if num == 1:
        print("Acceptable: x>0, y>0")
    if num == 2:
        print("Acceptable: x<0, y>0")
    if num == 3:
        print("Acceptable: x<0, y<0")
    if num == 4:
        print("Acceptable: x>0, y<0")
    if num >= 5:
        print("Error")


print_answer(number)
