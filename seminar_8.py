# (имя файла, режим, код чтения) даем имя файлу для открытия
# with open('example.txt', 'r', encoding='utf-8') as file: 
    # прочистали перенеси все данные в аргумент text
    # text = file.read() 
    # print(text)

    # for letter in text:
    #     print(letter) # вывели данные по буквам

    # text = file.read().splitlines() # вывели данные списком из слов
    # print(text)
    # print(type(text))

    # text = file.readlines() # вывели данные списком из слов c \n
    # print(text)
    # print(type(text))

# Для больших объемов данных, чтобы не заполнять всю оперативную память
# счистываем одну строку. забываем её, потом считываем другую и т.д.
# Пример ниже:


    # line = file.readline()
    # while line: # пока строка не пустая
    #     print(line)
    #     line = file.readline()

# Задача.
# Посчитать кол-во символов в текстовом файле

# Вариант 1: (не очень)
""" kolvo = open('example.txt').read().count('а')
print(kolvo) """

# Вариант 2: (более правильный)
""" with open('example.txt', 'r', encoding='utf-8') as file:
    symbol = input('Введите символ для поиска: ')
    print(file.read().count(symbol)) """

# Задача: Создать файл result.txt и записать в него вводимую строку some_list

""" some_list = [1, 2, 3, 4, 5, 6]
with open('result.txt', 'w', encoding='utf-8') as file:
    for el in some_list:
        file.write(str(el) + '\n') """

# Задача: Посчитать длину первой строки в файле example.txt, и в файл result.txt
# записать все строки с такой же длиной,
# как у первой строки.

# with open('example.txt', 'r', encoding='utf-8') as file:
#     text_list = file.read().splitlines() # нашлипервую строку
#     first_len = len(text_list[0]) #посчитали кол-во символов первой строки (индекс 0)
#     print(first_len)
#     result_list = [i for i in text_list if len(i) == first_len] # ищем строки с таким же кол-вом символов
#     with open('result.txt', 'w', encoding='utf-8') as res: # открываем файл result.txt и даем ему кличку res
#         for el in result_list: # для совпаений из списка result_list
#             res.write(el + '\n')  # записываем совпадения в result.txt под кличкой res
