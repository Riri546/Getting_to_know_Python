# 5. A number is given. Check whether it is a multiple of 5 and 10 or 15, but not 30

num = int(input('Enter an integer: '))


def find(number):
    if number % 30 != 0:
        if number % 5 == 0 and number % 10 == 0 or number % 15 == 0:
            return "The number is a multiple of"
    return "The number is not a multiple"

print(find(num))
