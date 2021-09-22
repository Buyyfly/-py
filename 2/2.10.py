# Задача-10:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# Решение реализовать в виде функции.


# Изменим немного решение по задаче 1.7
def chet(zn):
    if sum(zn[:3]) == sum(zn[3:6]):
        return 'Билет счастливый'
    else:
        return 'Билет не счастливый'


def vvod():
    while True:
        try:
            a = ' '.join(input('Введите 6ти значный номер билета: ')).split()
            if len(a) != 6:
                print('Билет должен быть 6ти значный.')
                continue
            return [int(i) for i in a]
        except ValueError:
            print('Не корректный ввод.')


print(chet(vvod()))