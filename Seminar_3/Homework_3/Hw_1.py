# 1.Specify a list of several numbers. Write a program that will find the sum of the list items standing in an odd position.
# *Example:*
# - [2, 3, 5, 8, 3, 1] -> on the odd positions of elements 3 and 9 the answer is: 12


int_list = []
for element in input('Enter integers in the list separated by a space: ').split():
    int_list.append(int(element))
print(int_list)


def sum_list(int_l, sum_odd):
    length = len(int_l)
    print(f'List length = {length}')
    for i in range(0, length):
        if i % 2 != 0:
            sum_odd += int_l[i]
    print(f'The sum of all the odd numbers in the list: {sum_odd}')


sum_list(int_list, 0)
