# Задача-7:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Билет считается счастливым, если сумма его первых и последних цифр равны.


while True:
    a = ' '.join(input('Введите число 6ти значный номер билета: ')).split()
    try:
        a = [int(i) for i in a]
        break
    except ValueError:
        print('Не корректный ввод. Билет должен быть формата "123456".')

if sum(a[0:3]) == sum(a[3:6]):
    print('Счастливый билет.')
else:
    print('Не счастливый билет.')
