"""Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке
[-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции.
По возможности доработайте алгоритм (сделайте его умнее)."""
import random


def my_sort(my_list: list):
    n = 1
    while n < len(my_list):
        for i in range(len(my_list) - n):
            if my_list[i] < my_list[i + 1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
        n += 1
    return my_list


sample_list = [random.randint(1, 100) for i in range(15)]
print('первоначальный список : ', sample_list)
my_sort(sample_list)
print('первоначальный список : ', sample_list)


# def bubble_sort(lst):
#     n = 1
#
#     while n < len(lst):
#         count = 0
#
#         for i in range(len(lst) - 1 - (n - 1)):
#
#             if lst[i] < lst[i + 1]:
#                 lst[i], lst[i + 1] = lst[i + 1], lst[i]
#                 count += 1
#
#         if count == 0:
#             break
#
#         n += 1
