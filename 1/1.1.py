# Задача-1:
# Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.

a = input('Ведите значение 1-ой переменной:')
b = input('Ведите значение 2-ой переменной:')
c = a
a = b
b = c
print(f'{a} {b}')