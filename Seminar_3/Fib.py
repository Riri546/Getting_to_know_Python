def fib(n):
    print(n)
    if n == 0:
        return 0
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)


print('-' * 15)
print(fib(4))
