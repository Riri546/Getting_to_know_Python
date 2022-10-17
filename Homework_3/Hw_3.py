# 3.Specify a list of real numbers. Write a program that will find the difference between the maximum 
# and minimum values of the fractional part of the elements.
# *Example:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

source_list = [1.1, 1.2, 3.1, 5, 10.01]
print(source_list)

print(f'Maximum value of the list: {max(source_list)}')
print(f'Maximum value of the list: {min(source_list)}')

print(f'The difference between the maximum and minimum values: {max(source_list)-min(source_list)}')
    