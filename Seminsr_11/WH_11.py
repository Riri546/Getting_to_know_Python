from sympy import *
# import matplotlib.pyplot as plt


print('1. Определить корни ')
x = Symbol('x')
func = 5*x**2+10*x-30
y = solve(func)
x1 = round(float(y[0]),2)
x2 = round(float(y[1]),2)
print(f'Ответ: x1 = {x1}, x2 = {x2}')


print('2. Интервалы, на котрых функция возрастает')
fd = diff(func)
print(f'Ответ: {solve(0 < fd)}')

print('3. Интервалы, на котрых функция убывает')
print(f'Ответ: {solve(fd < 0)}')

print('4. Построить график')
