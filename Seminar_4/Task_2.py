# 2 Find the roots of the quadratic equation Ax2 + Bx + C = 0 in two ways:
# 1) using mathematical formulas for finding the roots of a quadratic equation;
# 2) using additional Python libraries.

a = int(input('Enter the number a: '))
b = int(input('Enter the number b: '))
c = int(input('Enter the number c: '))

list1 = (a, b, c)


def difsciminant(linput_list):
    a, b, c = linput_list
    d = b ** 2 - 4 * a * c
    if d == 0:
        x1 =  -b / 2 * a 
        return x1
    elif d > 0:
        x1 = (-b + d ** 0.5) / 2 * a
        x2 = (-b - d ** 0.5) / 2 * a
        return x1, x2
    else:
        print('The equation has no roots')
        
print(difsciminant(list1))