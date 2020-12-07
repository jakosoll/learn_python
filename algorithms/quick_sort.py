"""
Алгоритм быстрой сортировки
1. Так как алгоритм основан на рекурсии, нужно сразу прописать базовый случай
Проверяем длину списка, если там один элемент (т.е. меньше двух), то возвращаем его
2. Нужно извлечь опорный элемент. Это будет именно элемент и он будет списком.
Можно и нужно брать рандомный элемент. Для этого используется randrange,
потому что он не возвращает последний элемент
3. Нужно создать списки элементов меньше и больше опорного элмента. Используем для этого list comprehension по условю
4. Возвращаем рекурсивный вызов функции с меньшими элментами, потом прибавляем опорный элмент и следом функцию
 с списком меньших элементов
"""
import random


def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot: list = [array[random.randrange(0, len(array))]]
        first_array: list = [i for i in array if i < pivot[0]]
        second_array: list = [i for i in array if i > pivot[0]]
        return quick_sort(first_array) + pivot + quick_sort(second_array)


mylist = ['sergey', 'anna', 'tatyana', 'steve', 'alina', 'govard', 'ben', 'ronald', 'fred', 'valera', 'roman']
assert quick_sort(mylist)[0] == 'alina'
assert quick_sort(mylist)[1] == 'anna'
print(quick_sort(mylist))

