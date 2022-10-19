# 1. Specify a string from a set of numbers. Write a program that will show a larger and
# smaller number. Use a space as the separator character.

us_list = []
for element in input('Enter integers in the list separated by a space: ').split():
    us_list.append(int(element))
print(us_list)

print(f'Min: {min(us_list)}')
print(f'Max: {max(us_list)}')