# 3.Specify a list of real numbers. Write a program that will find the difference between the maximum
# and minimum values of the fractional part of the elements.
# *Example:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from itertools import count
import math


source_list = [1.1, 1.2, 3.1, 5, 10.01]
print(source_list)

int_lst = map(source_list)
print(int_lst)

# def max_min(max_l, min_l, s_l):
#     for i in s_l:
#         if i - int(i) >= max_l:
#             max_l = i - int(i)
#         if i - int(i) <= min_l:
#             min_l = i - int(i)
#     print(
#         f'The difference between the maximum and minimum values: {max_l - min_l}')


# max_min(0, 1, source_list)
