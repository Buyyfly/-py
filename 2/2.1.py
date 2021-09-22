# Задача-1:
# Дано произвольное целое число, вывести поочередно цифры исходного числа

while True:
    try:
        a = input('Введите целое цисло = ')
        int(a)
        break
    except ValueError:
        print('Не корректный ввод.')

a = ' '.join(a).split()
print(type(a))
for i, el in enumerate(a):
    print(f'Число №{i + 1} = {el}')