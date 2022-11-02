# 3. Specify two numbers. Write a program that will find the NOC (smallest common
# multiple) of these two numbers.


from http.client import NETWORK_AUTHENTICATION_REQUIRED


x = int(input('Enter the number x: '))
y = int(input('Enter the number y: '))


def nod(a, b):
    if b == 0:
        return a
    else:
        return nod(b, a % b)
print(f'NOD = {nod(x, y)}')


noki = lambda a, b: int(abs(a * b) / nod(a, b))
print(f'NOC = {noki(x, y)}')

# def nok(a, b):
#     return int(abs(a * b) / nod(a, b))
# print(f'NOC = {nok(x, y)}')


