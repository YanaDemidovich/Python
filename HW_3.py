# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

""" some_list = [int(input("Введите число: ")) for _ in range(int(input("Введите кол-во чисел: ")))]
a = int(input("Введите число для поиска: "))
count = 0
for ind in range(0, len(some_list)):
    if some_list[ind] == a:
        count += 1
print(count) """


# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

""" some_list = [int(input("Введите число: ")) for _ in range(int(input("Введите кол-во чисел: ")))]
a = int(input("Введите число для поиска: "))
list_b = []
for ind in range(len(some_list)): # создаем список со значениями разницы
    b = a - some_list[ind]
    list_b.append(b)
print(list_b)
minb = list_b[0] # находим мин.разницу между числами
for i in list_b:
    if i < minb:
        minb = i
print(list_b.index(minb)) # выводим индекс числа с мин.разницей
print(some_list[list_b.index(minb)]) # выводим число с индексом мин.разницы """


""" x = [1, 2, 3, 5.5, 17.0, 0.32, 22, 1000.222]
print(x.index(min(x)) + min(x)) """

# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так: A, E, I, O, U, L, N, S, T, R – 1 очко; 
# D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; 
# Q, Z – 10 очков. А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
# Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; 
# Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, 
# либо только русские буквы.
# *Пример:*
# ноутбук
#     12
 
 