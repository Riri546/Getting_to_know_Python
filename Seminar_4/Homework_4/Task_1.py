# 1. Specify a string from a set of numbers. Write a program that will show a larger and
# smaller number. Use a space as the separator character.

us_list = []
for element in input('Enter integers in the list separated by a space: ').split():
    us_list.append(int(element))
print(us_list)

print(f'Minimum value of the list: {min(us_list)}')
print(f'Maximum value of the list: {max(us_list)}')