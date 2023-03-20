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

def merge_sort(nums):
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
print(list1)