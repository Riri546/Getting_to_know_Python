# 3. Write a program in which the user will set two lines, and the program
# will determine the number of occurrences of one line in another.

first_string = input('Enter the first line: ')
second_string = input('Enter the second line: ')
print(f'The number of occurrences of one line in the first: {first_string.count(second_string)}')