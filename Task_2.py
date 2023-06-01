# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X


import random

n = int(input('Введите размер массива: '))
x = int(input('Введите искомое число: '))
array = []
for i in range(n):
    array.append(random.randrange(n))
print(array)


def near(array, number):
    return min(array, key=lambda x: abs(number - abs(x)))
print(f'Ближайшее к числу {x} - число: {near(array, x)}')
