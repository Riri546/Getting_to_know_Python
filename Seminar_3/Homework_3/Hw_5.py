# 5.Set the number. Make a list of Fibonacci numbers, including for negative indices.
# *Example:*
# - for k = 8 , the list will look like this: [-21 ,13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# [ Negafibonacci] (https://ru.wikipedia.org/wiki/Негафибоначчи )

num = int(input('Enter num: '))


def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def negafibonacci(n):
    list_f = []
    for i in range(1, n + 1):
        fibon_i = fibonacci(i)
        list_f.append(fibon_i)
        if i != 1:
            list_f.insert(0, (-1) ** i * fibon_i)
    print(list_f)

negafibonacci(num)