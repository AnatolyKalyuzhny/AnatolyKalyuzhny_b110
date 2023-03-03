#Получить список четных чисел из другого заданного списка чисел.
import random
random_list = [random.randint(-20, 40) for _ in range(20)]
print(random_list)
new_list = [ x for x in random_list if x % 2 == 0]
print (new_list)

#Получить список квадратов чисел от 0 до 9.:
squares = [x**2 for x in range(10)]
print(squares)

#Получить список чисел от 0 до 10, кратных 2.
list = [x for x in range (11) if x % 2 ==0]
print (list)