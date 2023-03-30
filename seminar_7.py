# Функция поиска квадрата числа

""" def f(x):
    return x*x

x = int(input("Введите число х: "))
print(f(x))
print(type(f))

a = f  # переименовали функцию 
print(a(x))
print(type(a)) """

# Калькулятор
# Вариант с одним аргументом

""" def calc1(a):   # операция сложения
    return a+a

def calc2(a):   # операция умножения
    return a*a

def math(op, x):    # операция, аргумент
    print(op(x))    # выводим результат операции с аргументом (x)

math(calc1, 5)      # вызов функции math """

# Вариант с двумя аргументами

""" def calc1(a, b):   # операция сложения
    return a + b

def calc2(a, b):   # операция умножения
    return a * b

def math(op, x, y):    # операция, аргументы x и y
    print(op(x, y))    # выводим результат функции с 
                       # указанной операцией и аргументами (x, y)

math(calc2, 5, 2)      # вызов функции math """

# lambda функция

""" def math(op, x, y):    # операция, аргументы x и y
    print(op(x, y)) """

# 1 вариант функции calc1
""" def calc1(a, b):
    return a + b """

# 2 вариант функции calc1
""" calc1 = lambda a, b: a + b
math(calc1, 5, 2) """

# 3 вариант функции calc1
""" math(lambda a, b: a + b, 5, 2) """ # можно сразу без указания названия прописать функцию в вывове ответа


# Зада 1: В списке хранятся числа.
# Нужно выбрать только четные числа и составить список пар (число; квадрат числа)
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)]

# 1-ый вариант решения
""" data = [1, 2, 3, 5, 8, 15, 23, 38]  # дан список чисел
res = list()                        # создали пустой список

for i in data:                      # для элемента из списка data
    if i % 2 == 0:                  # если элемент делится на 2 и остаток равен 0
        res.append([i, i**2])       # вносим в конец спика res сам элемент и его квадрат
print(res) """

# 2-ой вариант решения с использованием lambda функции

""" def select(f, col):
    return [f(x) for x in col]   # возвращает список, в котором мы к каждому элементу применили функцию f

def where(f, col):               
    return [x for x in col if f(x)]  # возвращает только те значения, которые прошли проверку условием f от x

data = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, data)   # создали список из входных чисел
print(res)
res = where(lambda x: x % 2 == 0, res) # отобрали четные числа из списка res
print(res)
res = list(select(lambda x: (x, x**2), res)) # из списка четных чисел res создали картэж, где выводит само число и его квадрат
print(res) """


## Функция map
# map "НАЗВАНИЕ ФУНКЦИИ"(lambda x: x + 10 "САМА ФУНКЦИЯ, КОТОРУЮ ХОТИМ ПРИМЕНИТЬ К ОБЪЕКТУ", list_1 "САМ ОБЪЕКТ"))

""" list_1 = [x for x in range(1, 10)]
print(list_1)

list_1 = list(map(lambda x: x + 10, list_1))
print(list_1) """

# Задача 2: C клавиатуры вводится некий набор чисел, в качестве разделителя
# используется пробел. Этот набор чисел будет считан в качестве строки. Как
# превратить list строк в list чисел?

""" data = '15 156 96 3 5 8 52 5'  # это строка
print(data)
print(type(data))
# data = list(data) # так получится список из строк
# print(data)
# print(type(data))

data = list(map(int, data.split())) # преобразовали строку в список из чисел типа int
print(data)
print(type(data))
 """
# Применим функцию map к задаче 1.
# Вместо функции select применим map
# Удаляем саму функцию select и дальше в коде вместо указания select пишем map

""" def where(f, col):               
    return [x for x in col if f(x)]  # возвращает только те значения, которые прошли проверку условием f от x

data = [1, 2, 3, 5, 8, 15, 23, 38]
res = map(int, data)   # создали список из входных чисел
print(res)
res = where(lambda x: x % 2 == 0, res) # отобрали четные числа из списка res
print(res)
res = list(map(lambda x: (x, x**2), res)) # из списка четных чисел res создали картэж, где выводит само число и его квадрат
print(res) """


# Функция filter

""" data = [15, 10, 37, 45, 295]
res = list(filter(lambda x: x % 10 == 5, data))
print(res) """

# Применим функцию filter к задаче 1.
# Вместо функции where применим filter
# Удаляем саму функцию where и дальше в коде вместо where пишем filter


""" data = [1, 2, 3, 5, 8, 15, 23, 38]
res = map(int, data)   # создали список из входных чисел
res = filter(lambda x: x % 2 == 0, res) # отобрали четные числа из списка res
res = list(map(lambda x: (x, x**2), res)) # из списка четных чисел res создали картэж, где выводит само число и его квадрат
print(res)
 """

### Функция zip
# пробегает по минимальному входящему набору

""" users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
data = list(zip(users, ids))
print(data) """ # [('user1', 4), ('user2', 5), ('user3', 9), ('user4', 14), ('user5', 7)]

### Функция enumerate() 
# применяется к итерируемому объекту и
# возвращает новый итератор с кортежами из индекса и элементов входных
# данных.
# Позволяет пронумеровать набор данных

""" users = ['user1', 'user2', 'user3']
data = list(enumerate(users))
print(data) """ # [(0, 'user1'), (1, 'user2'), (2, 'user3))]

### ФАЙЛЫ ###
# Варианты режима (мод):
# 1. a – открытие для добавления данных.
# ○ Позволяет дописывать что-то в имеющийся файл.
# ○ Если вы попробуете дописать что-то в несуществующий файл, то файл
# будет создан и в него начнётся запись.
# 2. r – открытие для чтения данных.
# ○ Позволяет читать данные из файла.
# ○ Если вы попробуете считать данные из файла, которого не существует,
# программа выдаст ошибку.
# 3. w – открытие для записи данных.
# ○ Позволяет записывать данные и создавать файл, если его не
# существует.
# Миксованные режимы:
# 4. w+
# ○ Позволяет открывать файл для записи и читать из него.
# ○ Если файла не существует, он будет создан.
# 5. r+
# ○ Позволяет открывать файл для чтения и дописывать в него.
# ○ Если файла не существует, программа выдаст ошибку.


## режим a
""" colors = ['red', 'green', 'blue']
data = open('file.txt', 'a') # здесь указываем режим, в котором будем работать
data.writelines(colors) # разделителей не будет
data.close() """

# data.close() — используется для закрытия файла, чтобы разорвать
# подключение файловой переменной с файлом на диске.
# exit() — позволяет не выполнять код, прописанный после этой команды в
# скрипте.

## режим w
""" with open('file.txt', 'w') as data:
    data.write('line 1\n')
    data.write('line 3\n') """

## режим r
""" path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close() """

# Задача 1.
# Создайте список из случайных чисел.
# Найдите номер его последнего локального максимума (локальный максимум
# это элемент, который больше любого из своих соседей)

# Вариант 1. Прохождения по индексам с начала списка
""" import random

find_ind = -1
our_list = [random.randint(1, 10) for _ in range(10)] # сделали рандомный список

print(our_list)
for ind in range(1, len(our_list) - 1):
    if our_list[ind - 1] < our_list[ind] > our_list[ind + 1]:
        find_ind = ind
if find_ind != 1:
    print(find_ind + 1)
else:
    print("Локальных максимумов нет") """

# Вариант 2. Прохождения по индексам с конца списка
""" import random

our_list = [random.randint(1, 10) for _ in range(10)] # сделали рандомный список

print(our_list)
for ind in range(len(our_list) - 2, 0, -1):
    if our_list[ind - 1] < our_list[ind] > our_list[ind + 1]:
        print(ind + 1)
        break
else:
    print("Локальных максимумов нет") """

# Задача 2.
# Создайте список из случайных чисел.
# Найдите максимальное кол-во его одинаковых элементов

# Вариант 1.
""" import random
our_list = [random.randint(1, 10) for _ in range(10)]
print(our_list)

count_dict = {}  #создали пустой словарь
for el in our_list:
    if el not in count_dict:
        count_dict[el] = 1
    else:
        count_dict[el] += 1
print(count_dict)
print(max(count_dict.values())) """

# Вариант 2.
""" import random
our_list = [random.randint(1, 10) for _ in range(10)]
print(our_list)

max_count = 0
used_set = set() #создаем пустое множество

for el in our_list:
    if el not in used_set:
        if our_list.count(el) > max_count:
            max_count = our_list.count(el)
        used_set.add(el)
print(max_count) """


# Задача 3.
# Создайте список из случайных чисел.
# Найдите второй максимум.
# Пример:
# a = [1, 2, 3] -> первый максимум == 3, второй максимум == 2

""" import random
our_list = [random.randint(1, 10) for _ in range(10)]
print(our_list)

our_list = list(set(our_list)) # создали из списка множество, чтобы удалить повторы
first_max = our_list[0]
second_max = our_list[1]
if first_max < second_max:
    first_max, second_max = second_max, first_max
for el in our_list:
    if el > first_max:
        first_max, second_max = el, first_max
    elif el > second_max:
        second_max = el
print(second_max) """


# Задача 4.
# Создайте список из случайных чисел.
# Найдите кол-во различных элементов в нем

""" import random
our_list = [random.randint(1, 10) for _ in range(10)]
print(our_list)

our_list = set(our_list) # создали из списка множество, чтобы удалить повторы
print(our_list)
print(len(our_list)) """