# 2. Write a program that accepts the number N as input and outputs a set of products of numbers from 1 to N.
# *Example:*
# N = 4, then [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

number = int(input('Enter the natural number n: '))
result = []


def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
    print (n[i])

def print_list(n):
    if factorial(n) !=0:
        result = [factorial]
    print(result)


print(factorial(number))
print(print_list(number))