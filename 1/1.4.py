# Задача-4:
# Напишите программу, вычисляющую корни квадратного уравнения вида: ax2 + bx + c = 0.
# Параметры уравнения вводите с помощью функции input()

import math


def vvod(znc):
    try:
        return int(input(f'Ведите значение {znc}:'))
    except ValueError:
        print('Не корректный ввод.')


while True:  # В задаче указано только про квадратные уравнения.
    a = vvod('a')
    if a != 0:
        break
    else:
        print('Для квадратного уравнения значение "а" не может равняться "0".')

b = vvod('b')
c = vvod('c')
d = (b ** 2) - (4 * a * c)
if d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print(f'Корни уравнения:\nx1 = {round(x1, 2)}\nx2 = {round(x2, 2)}')
elif d == 0:
    x12 = -b / (2 * a)
    print(f'Корни уравнения равны.\nx1 = x1 = {round(x12, 2)}')
else:
    print(f'У уравнения нет корней.')
