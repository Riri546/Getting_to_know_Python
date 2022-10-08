# 3.Specify a list of n numbers in the sequence $(1+\frac 1 n)^n$ and display their sum on the screen.
# *Example:*
# - For n = 6:
#     [2.0, 2.25, 2.3704, 2.4414, 2.4883, 2.5216]
#     Sum of numbers = 14.0717

number = input('Enter number: ')
sum_result = 0
result = []


def filling_list(n, res):
    filling = 0
    for i in range(0, n):
        filling = ((1+(n/1))**n)
        res.append(filling)
    print(res)


def sum_number(sum, n):
    for i in n:
        sum += i
    print(f'Sum of numbers: {sum}')


filling_list(number, result)
sum_number(sum_result, number)
