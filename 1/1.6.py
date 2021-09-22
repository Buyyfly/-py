# Задача-6:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.


# Поменяем наименование точек на A B C D для удобства
# Будем руководствоваться один из правил AB = CD, BC = AD

import math


def chet(x1, x2, y1, y2):
    return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))  # Формула отрезка длинны


def vvod(znc):
    while True:
        try:
            return float(input(f'{znc} = '))
        except ValueError:
            print('Не корректный ввод. Повторите.')


xa = 1
ya = 1
xb = 1
yb = 2
xc = 2
yc = 2
xd = 2
yd = 1

if chet(xa, xb, ya, yb) == chet(xc, xd, yc, yd) \
        and chet(xb, xc, yb, yc) == chet(xa, xd, ya, yd):
    print('Это параллелограмм.')
else:
    print('Это не параллелограмм.')

