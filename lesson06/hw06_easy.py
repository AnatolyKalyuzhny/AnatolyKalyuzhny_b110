# Задача-1:
# Следующая программа написана верно, однако содержит места потенциальных ошибок.
# используя конструкцию try добавьте в код обработку соответствующих исключений.
# Пример.
# Исходная программа:
def avg(a, b):
    """Вернуть среднее геометрическое чисел 'a' и 'b'.

    Параметры:
        - a, b (int или float).

    Результат:
        - float.
    """
    return (a * b) ** 0.5
a = (input("a = "))
b = (input("b = "))
while type(a and b) != float:
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        print('введено неверное значение, введите числа')
        a = (input("a = "))
        b = (input("b = "))
c = avg(a, b)
print("Среднее геометрическое = {:.2f}".format(c))

# ПРИМЕЧАНИЕ: Для решения задач 2-4 необходимо познакомиться с модулями os, sys!
# СМ.: https://pythonworld.ru/moduli/modul-os.html, https://pythonworld.ru/moduli/modul-sys.html

# Задача-2:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os

# Создаем
for i in range(1, 10):
    dir_name = f"dir_{i}"
    os.makedirs(dir_name, exist_ok=True)
#удаляем
for i in range(1, 10):
    dir_name = f"dir_{i}"
# Задача-3:
# Напишите скрипт, отображающий папки текущей директории.
import os
files_and_folders = os.listdir()
# отделить папки
for item in files_and_folders:
    if os.path.isdir(item):
        print(item)

# Задача-4:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import os
import shutil # я так понимаю, что без этого модуля, нужно будет дополнительно открывать файл
              # и читать его

current_file = os.path.abspath(__file__)
file_name, file_extension = os.path.splitext(current_file)
new_file_name = file_name + "_copy" + file_extension

# Создаем копию файла
shutil.copyfile(current_file, new_file_name)
print(new_file_name)