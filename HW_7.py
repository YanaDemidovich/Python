# Задача 34:
# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, 
# насколько легко он их придумывает, Вам стоит написать программу. 
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) 
# в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, 
# если во фразе несколько слов, 
# то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, 
# если с ритмом все не в порядке. Используйте split()


""" stih = (str(input("Введите стихотворение: ")))
print(stih)

b = stih.split()
print(b)
#дальше не знаю как...((

print(list(map(len, b))) """ # посчитала кол-во символов в каждом элементе



# Задача 36.
# Создайте список из случайных чисел.
# Найдите кол-во различных элементов в нем

import random
our_list = [random.randint(1, 10) for _ in range(10)]
print(our_list)

our_list = set(our_list) # создали из списка множество, чтобы удалить повторы
print(our_list)
print(len(our_list))