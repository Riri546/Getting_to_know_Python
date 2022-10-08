# 2. Write a program that accepts the number N as input and outputs a set of products of numbers from 1 to N.
# *Example:*
# N = 4, then [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input('Enter the natural number n: '))
factorial = 1
result = []

for i in range(1, n + 1):
    factorial *= i
    result.append(factorial)
print(result)


