# 5.Set the number. Make a list of Fibonacci numbers, including for negative indices.
# *Example:*
# - for k = 8 , the list will look like this: [-21 ,13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# [ Negafibonacci] (https://ru.wikipedia.org/wiki/Негафибоначчи )
num = int(input('Enter num: '))
list_f = []


def fibonacci(n):
    if n == 0:
        return 0
    if n in [1, 2]:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
        
    


def negafibonacci(n):

    if n == 1:
        return 1
    if n == 2:
        return -1
    else:
        return fibonacci(n+1) - fibonacci(n+2)


print(fibonacci(num))
print(negafibonacci(num))
