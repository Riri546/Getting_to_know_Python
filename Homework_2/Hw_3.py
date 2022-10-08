# 3.Specify a list of n numbers in the sequence $(1+\frac 1 n)^n$ and display their sum on the screen.
# *Example:*
# - For n = 6:
#     [2.0, 2.25, 2.3704, 2.4414, 2.4883, 2.5216]
#     Sum of numbers = 14.0717

number = int(input('Enter number: '))
sum_result = 0


def filling_list(num):
    result = []
    for n in range(1, num+1):
        filling = (1+1/n)**n
        result.append(filling)
    print(f'List: {result}')
    return result


print('Sum of numbers:', sum(filling_list(number)))
