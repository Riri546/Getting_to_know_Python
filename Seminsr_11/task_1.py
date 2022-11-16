from sympy import *
import matplotlib.pyplot as plt


print('1. Определить корни ')
x = Symbol('x')
func = 5 * x ** 2 + 10 * x - 30
y = solve(func)
x1 = round(float(y[0]), 2)
x2 = round(float(y[1]), 2)
print(f'Ответ: x1 = {x1}, x2 = {x2}')


print('2. Интервалы, на котрых функция возрастает')
fd = diff(func)
print(f'Ответ: {solve(0 < fd)}')


print('3. Интервалы, на котрых функция убывает')
print(f'Ответ: {solve(fd < 0)}')


print('4. Построить график')
list_y = []
for i in range(-5, 6):
    x = i
    y = 5 * x ** 2 + 10 * x - 30
    list_y.append(y)
print(list_y)
plt.plot(range(-5, 6), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
plt.plot(range(-5, 6), list_y)
plt.grid()
plt.show()


print('5. Вычислить вершину')
corni = solve(fd)
top = corni[0]
x = top
y = 5 * x ** 2 + 10 * x - 30
print(f'Ответ: {top, y}')


print('6. Определить промежутки, на которым f > 0')
print(f'Ответ: {solve(0 < func)}')


print('7. Определить промежутки, на которым f < 0')
print(f'Ответ: {solve(func < 0)}')
