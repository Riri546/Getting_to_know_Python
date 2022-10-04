# 3. Display the numbers from -N to N.

num = int(input('Enter an integer: '))


def print_num(number):
    number = abs(number)
    first = number * -1
    second = number
    while first <= second:
        print(f'{first}, ', end='')
        first += 1


print_num(num)
