# 5.Set the number. Make a list of Fibonacci numbers, including for negative indices.
# *Example:*
# - for k = 8 , the list will look like this: [-21 ,13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# [ Negafibonacci] (https://ru.wikipedia.org/wiki/Негафибоначчи )

fib1 = fib2 = 1

fib = []

n = int(input('Enter number: '))


print(fib1, fib2, end=' ')

for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end = ' ')

for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end = ' ')
