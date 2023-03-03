# # Задача-1: Ввести ваше имя и возраст в отдельные переменные,
# # вычесть из возраста 18 и вывести на экран в следующем виде:
# # "Василий на 2 года/лет больше 18"
# # по желанию сделать адаптивный вывод, то есть "на 5 лет больше", "на 3 года меньше" и.т.д.
# UPD добавил цикл и обработку исключений, в случае ввода некорректного значения, оба варианта с циклом работают

# первый вариант

age = input('введите ваш возраст:')
while type(age) != int:
    try:
        age = int(age)
    except ValueError:
        print('введено неверное значение, повторите ввод')
        age = input('введите ваш возраст:')

if age == 18:
    name = (input('введите ваше имя:'))
    print(f'{name}, Ваш возраст 18, поздравляем!')
    print('что то не так')
    import time
    time.sleep(2)  # Сон в 2 секунды
    import webbrowser
    webbrowser.open_new_tab('https://papik.pro/uploads/posts/2021-11/1636144028_18-papik-pro-p-pornokhab-logotip-foto-19.jpg')
elif age > 18:
    name = (input('введите ваше имя:'))
    result = age - 18
    print(f'{name}, Ваш возраст на {result} больше 18, поздравляем!!!')
    import time
    time.sleep(1)  # Сон в 2 секунды
    import webbrowser
    webbrowser.open_new_tab('https://papik.pro/uploads/posts/2021-11/1636144028_18-papik-pro-p-pornokhab-logotip-foto-19.jpg')
elif age < 18:
    result = 18 - age
    print(f'Ваш возраст на {result} меньше 18, увы и ах!')
    import time
    time.sleep(2)  # Сон в 2 секунды
    import webbrowser
    webbrowser.open_new_tab('https://media.baamboozle.com/uploads/images/69723/1623214673_223433_url.png')

# второй вариант

age = input('введите ваш возраст:')
while type(age) != int:
    try:
        age = int(age)
        if age == 18:
            name = (input('введите ваше имя:'))
            print(f'{name}, Ваш возраст 18, поздравляем!')
            print('что то не так')
            import time
            time.sleep(2)  # Сон в 2 секунды
            import webbrowser
            webbrowser.open_new_tab('https://papik.pro/uploads/posts/2021-11/1636144028_18-papik-pro-p-pornokhab-logotip-foto-19.jpg')
        elif age > 18:
            name = (input('введите ваше имя:'))
            result = age - 18
            print(f'{name}, Ваш возраст на {result} больше 18, поздравляем!!!')
            import time
            time.sleep(1)  # Сон в 2 секунды
            import webbrowser
            webbrowser.open_new_tab('https://papik.pro/uploads/posts/2021-11/1636144028_18-papik-pro-p-pornokhab-logotip-foto-19.jpg')
        elif age < 18:
            result = 18 - age
            print(f'Ваш возраст на {result} меньше 18, увы и ах!')
            import time
            time.sleep(2)  # Сон в 2 секунды
            import webbrowser
            webbrowser.open_new_tab('https://media.baamboozle.com/uploads/images/69723/1623214673_223433_url.png')
    except ValueError:
        print('введено неверное значение, повторите ввод')
        age = input('введите ваш возраст:')