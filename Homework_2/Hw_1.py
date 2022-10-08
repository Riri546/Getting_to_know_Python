# 1. Calculate the sum of digits in a real number.
# *Example:*
# - 6782 -> 23
# - 0,56 -> 11

number = input('Enter the natural number n: ')
sum = 0

print(f'Source string: {number}')
res_str = number.replace('.', '')
# Deleting all '.'
print(f'String after deleting all characters ".": {res_str}')

for i in res_str:
    if res_str != '.':
        sum += int(i)

print(f'Answer: {sum}')
