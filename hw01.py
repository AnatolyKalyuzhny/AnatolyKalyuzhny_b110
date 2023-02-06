
__author__ = 'Калюжный Анатолий Александрович.'

# # Задача-1: Ввести ваше имя и возраст в отдельные переменные,
# # вычесть из возраста 18 и вывести на экран в следующем виде:
# # "Василий на 2 года/лет больше 18"
# # по желанию сделать адаптивный вывод, то есть "на 5 лет больше", "на 3 года меньше" и.т.д.
#
# TODO: код пишем тут...
age = int(input('введите ваш возраст:'))
if age == 18:
    name = (input('введите ваше имя:'))
    print(name, ', Ваш возраст 18, поздравляем!')
    import time
    time.sleep(2)  # Сон в 2 секунды
    import webbrowser
    webbrowser.open_new_tab('https://papik.pro/uploads/posts/2021-11/1636144028_18-papik-pro-p-pornokhab-logotip-foto-19.jpg')
elif age > 18:
    name = (input('введите ваше имя:'))
    result = age - 18
    print(name,', Ваш возраст на', result,'больше 18, поздравляем!!!')
    import time
    time.sleep(1)  # Сон в 2 секунды
    import webbrowser
    webbrowser.open_new_tab('https://papik.pro/uploads/posts/2021-11/1636144028_18-papik-pro-p-pornokhab-logotip-foto-19.jpg')
elif age < 18:
    result = 18 - age
    print('Ваш возраст на', result, 'меньше 18, увы и ах!')
    import time
    time.sleep(2)  # Сон в 2 секунды
    import webbrowser
    webbrowser.open_new_tab('https://media.baamboozle.com/uploads/images/69723/1623214673_223433_url.png')
# # Задача-2: Исходные значения двух переменных запросить у пользоват еля.
# # Поменять значения переменных местами. Вывести новые значения на экран.
# # Подсказка:
# # * постарайтесь сделать решение через дополнительную переменную
# #   или через арифметические действия
# # Не нужно решать задачу так:
# # print("a = ", b, "b = ", a) - это неправильное решение!
#
# # TODO: код пишем тут...
# #
number_1 = 5
number_2 = 13
number_1, number_2 = number_2, number_1
print (number_1, number_2)

# # Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# # ax² + bx + c = 0.
# # Коэффициенты уравнения вводятся пользователем.
# # Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# # import math
# # math.sqrt(4) - вычисляет корень числа 4
#
# # TODO: код пишем тут...
import math

print ('введите значения для уравнения ax² + bx + c = 0:')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

D = b ** 2 - 4 * a * c
print ('Дискриминат D = ', D)

if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print ('x1 = ', x1, 'x2 = ', x2)
elif D == 0:
    x = -b / (2 * a)
    print ('x =',x )
else:
    print(' D < 0, корней нет')