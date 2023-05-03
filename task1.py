# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12


# list_1 = '2 4 6 8 10 12 10 8 6 4 2'.split()
# list_2 = '3 6 9 12 15 18'.split()

# from random import sample

# n = int(input("Введите величину первого списка > "))
# list_1 = sample(range(1, 50), n)
# print(list_1)
# m = int(input("Введите величину второго списка > "))
# list_2 = sample(range(1, 50), m)
# print(list_2)

# result_list = []
# for i in list_1:
#     for j in list_2:
#         if i == j:
#             result_list.append(i)
#             result_list.sort()
# print(set(result_list))

import random

n = int(input("Введите величину первого списка: "))
list_1 = [random.randint(0, 50) for i in range(n)]
print(list_1)

m = int(input("Введите величину второго списка: "))
list_2 = [random.randint(0, 50) for i in range(m)]
print(list_2)

result_list = list(set(list_1) & set(list_2))
result_list.sort()
print(result_list)