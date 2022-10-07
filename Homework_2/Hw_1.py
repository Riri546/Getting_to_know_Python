# 1. Calculate the sum of digits in a real number.
# *Example:*
# - 6782 -> 23
# - 0,56 -> 11

number = str(input('Enter a real number: '))

result = 0

for i in len(number):
    result = number[i]+number[i+1]
print('Answer {result}')