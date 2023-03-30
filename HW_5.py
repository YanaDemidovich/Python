# Задача 1
# Строка представляет собой арифметическое выражение из 
# однозначных чисел и знаков + и -. Вычислите результат.
# Пример^
# Ввод
# 8-5+2-1
# Вывод
# 4

# Вариант 1:
""" some_str = input("Введите арифметическое выражение: ")
result = 0
znak = ''
for el in some_str:
    if el.isdigit():
        if znak == "-":
            result -= int(el)
        else:
            result += int(el)
    else:
        znak = el
print(result) """

# Вариант 2:
""" some_list = input("Введите арифметическое выражение: ")
print(some_list)
print(eval(some_list)) """


# НЕОБЯЗАТЕЛЬНЫЕ

# Задача 26:  
# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

""" def number(a, b):
    if b == 0:
        return 1
    return (a ** b)

print(number(3, 5)) """


# Задача:
# Переносить текст по словам с каждой новой строки

# Вариант 1
""" some_str = input('Введите текст: ')
word = '' 
for letter in some_str:
    if letter != ' ':
        word += letter
    else:
        print(word)
        word = '' """

# Вариант 2
""" some_str = input('Введите текст: ')
print(*some_str.split(), sep='\n') """

