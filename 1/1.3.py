# Задача-3:
# Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]

while True:
    a = input('Введите список целых чисел через пробел: ').split()
    try:
        print(set([int(i) for i in a]))
        break
    except ValueError:
        print('Необходимо вводить только числа.')

