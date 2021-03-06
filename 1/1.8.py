# Задача-8:
# Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)
import datetime

import locale  # Для второго варианта вывода

locale.setlocale(locale.LC_ALL, '')

# Возьмем проверку из задания 1.5 (существование даты)
while True:
    a = input('Введите дату в формате "dd.mm.уууу":').split('.')
    if len(a) == 3:
        break
    else:
        print('Не корректный ввод.')

try:
    a = [int(i) for i in a]
    b = datetime.datetime(a[2], a[1], a[0])
    day = ['Первое', 'Второе', 'Третье',
           'Четвёртое', 'Пятое', 'Шестое',
           'Седьмое', 'Восьмое', 'Девятое',
           'Десятое', 'Одиннадцатое', 'Двенадцатое',
           'Тринадцатое', 'Четырнадцатое', 'Пятнадцатое',
           'Шестнадцатое', 'Семнадцатое', 'Восемнадцатое',
           'Девятнадцатое', 'Двадцатое', 'Двадцать первое',
           'Двадцать второе', 'Двадцать третье', 'Двадацать четвёртое',
           'Двадцать пятое', 'Двадцать шестое', 'Двадцать седьмое',
           'Двадцать восьмое', 'Двадцать девятое', 'Тридцатое',
           'Тридцать первое']
    month = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
             'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']

    print(f'Первый вариант с заранее созданным списком месяцев:\n'
          f'{day[int(a[0]) - 1]} {month[int(a[1]) - 1]} {a[2]} года')
    print(f'Второй вариант с месяцем на русском (день не получится изменить):\n'
          f'{day[int(a[0]) - 1]} {datetime.datetime.strftime(b, "%B")} {a[2]} года')
except ValueError as err:
    # Выведем текст ошибки чтобы понимать в чем она заключается, в некорректном вводе целого числа или
    # в том что даты такой не существует
    print(f'Ошибка:{err}')


