# 1. Write a program that accepts the number N as input and outputs a sequence of N terms.
# Example:
# - For N = 5: 1, -3, 9, -27, 81

n = int(input('Enter the natural number n: '))
result = ''
sigh = 1

for i in range(0, n):
    result += str(3 ** i * sigh)
    result += ', '
    sigh = - sigh
print(result[0:(len(result) - 2)])