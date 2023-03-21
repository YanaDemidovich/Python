""" import modul1

print(modul1.max1(5, 9)) """

# или

""" from modul1 import max1

print(max1(15, 9)) """

# или импортировать все функции

""" from modul1 import *

print(max1(15, 9)) """

# в рамках этого файла можно использовать название modul1 сокращенно
# присвоив ему другое имя, например "m1" через as

""" import modul1 as m1

print(m1.max1(5, 9)) """

## РЕКУРСИЯ на примере чисел Фиббоначи

""" def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n-1) + fib(n-2)

list_1 = []
for i in range(1, 10):
    list_1.append(fib(i))
print(list_1) """

## БЫСТРАЯ СОРТИРОВКА ПО ВОЗРАСТАНИЮ (при помощи рекурсии)
""" def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)
print(quick_sort([14, 5, 20])) """


## СОРТИРОВКА СЛИЯНИЕМ (при помощи рекурсии)

""" def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

list1 = [1, 5, 9, 5, 5, 45, 59, 2, 3, 71, 10]
merge_sort(list1)
print(list1) """


# Задача 25.
# Напишите программу, которая принимает на вход строку 
# и отслеживаете сколько раз данный символ встретится в строке.
# Если для такого символа кол-во повторов уже было выведено, 
# то второй раз выводить это кол-во уже не надо.
# Пример: ПРИВЕТ ПОКА
# П - 2, Р - 1, И - 1, В - 1, Е - 1, Т - 1, О - 1, К - 1, А - 1

""" some_str = input("Введите слово или фразу: ")
some_dict = {}           # создаем словарь
for letter in some_str:
    some_dict[letter] = some_dict.get(letter, 0) + 1
print(some_dict) """


# Задача.
# Пользователь вводит текст (строка). Словом считается последовательность 
# непробельных символов идущих подряд, слова разделены одним или большим числом пробелов 
# или символами конца строки.
# Определите, сколько различных слов содержится в этом тексте.

# Для облегчения используйте метод .split
# Метод .split для строк. Разделение строки по разделителю (пробелу)
# a = input()
# b = a.split()
# print(b)

""" some_str = input("Введите текст: ")
b = some_str.split()
print(b)
some_dict = {}           # создаем словарь
for letter in b:
    some_dict[letter] = some_dict.get(letter, 0) + 1
print(some_dict) """

# второй вариант решения, где убирает символы вконце слова - не буквы

""" a = input("Введите текст: ")
b = a.split()
for ind in range(0, len(b)):
    if not b[ind].isalpha():
        b[ind] = b[ind][0:-1]

c = set(b)
print(len(c)) """

# третий вариант решения, где убирает символы во всем тексте - не буквы

""" a = input("Введите текст: ")
b = a.split()
print(b)
for ind in range(0, len(b)):
    new_word = ''
    for letter in b[ind]:
        if letter.isalpha():
            new_word += letter
    b[ind] = new_word
print(b)
c = set(b)
print(len(c)) """


# Задача №29. 
# Ваня и Петя поспорили, кто быстрее решит 
# следующую задачу: “Задана последовательность 
# неотрицательных целых чисел. Требуется определить 
# значение наибольшего элемента 
# последовательности, которая завершается первым 
# встретившимся нулем (число 0 не входит в 
# последовательность)”. Однако 2  друга оказались не 
# такими смышлеными. Никто из ребят не смог до 
# конца сделать это задание. Они решили так: у кого 
# будет меньше ошибок в коде, тот и выиграл спор. За 
# помощью товарищи обратились к Вам, студентам.


# Ваня: сделали верный код
""" n = int(input())
max_number = n
while n != 0:
   n = int(input())
   if max_number < n:
       max_number = n
print(max_number) """

# Петя: 
""" n = int(input())
max_number = n
while n != 0:
   n = int(input())
   if max_number < n:
       max_number = n

print(max_number) """

