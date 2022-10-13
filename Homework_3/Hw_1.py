# 1.Specify a list of several numbers. Write a program that will find the sum of the list items standing in an odd position.
# *Example:*
# - [2, 3, 5, 9, 3] -> on the odd positions of elements 3 and 9, the answer is: 12

number = int(input('See a list of several natural numbers: '))
filling = []
filling.append(number)
print(filling)


def sum_num(fil):
    count = 0
    if fil % 2 != 0:
        count += fil
    print(f'Answer = {count}')


sum_num(filling)
