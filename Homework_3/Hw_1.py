# 1.Specify a list of several numbers. Write a program that will find the sum of the list items standing in an odd position.
# *Example:*
# - [2, 3, 5, 9, 3] -> on the odd positions of elements 3 and 9, the answer is: 12

from itertools import count


int_list = []
for element in input('Enter integers in the list separated by a space: ').split():
    int_list.append(int(element))
print(int_list)


def sum_list(int_l):
    length = len(int_l)
    print(f'List length = {length}')
    print(type(length))
    count = 0
    for i in range(length+1):
        if i % 2 != 0:
            count += i
    print(f'Answer: {count}')
    return count


sum_list(int_list)
