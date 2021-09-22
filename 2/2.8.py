# Задача-8:
# Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random:
# import random
# random.randint(-100, 100)

import random

while True:
    try:
        n = int(input('Введите кол-во элементов: '))
        break
    except ValueError:
        print('Не корректный ввод.')


i = 0
a = []
while n > i:
    a.append(random.randint(-100, 100))
    i += 1
print(a)