# Задача-7:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

import math

while True:
    try:
        a = input('Введите список целых чисел через пробел: ').split()
        a = [int(i) for i in a]
        break
    except ValueError:
        print('Не корректный воод.')


b = [int(math.sqrt(i)) for i in a if i > 0 and float.is_integer(math.sqrt(i))]
print(b)