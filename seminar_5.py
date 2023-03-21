# Задача №33. 
# Хакер Василий получил доступ к классному журналу и 
# хочет заменить все свои минимальные оценки на 
# максимальные. Напишите программу, которая 
# заменяет оценки Василия, но наоборот: все 
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

""" marks_list = [int(input("Введите оценку: ")) for _ in range(int(input("Введите кол-во оценок: ")))]
max = marks_list[0]
min = marks_list[0]
for el in marks_list:
    if el < min:
        min = el
    if el > max:
        max = el
for ind in range(0, len(marks_list)):
    if marks_list[ind] == max:
        marks_list[ind] = min
print(marks_list) """

##### какая-то ерунда вышла

# Задача №35. 
# Напишите функцию, которая принимает одно число и 
# проверяет, является ли оно простым

# Напоминание: Простое число - это число, которое 
# имеет 2 делителя: 1  и n(само число)

# Input: 5
# Output: yes 

def simpel_number(number):
    for i in range(2, number // 2 +1):
        if number % i == 0:
            return "Число не простое"
        return "Число простое"
print(simpel_number(11))

