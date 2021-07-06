"""Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке
[-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции.
По возможности доработайте алгоритм (сделайте его умнее)."""
import random


def my_sort(my_list: list):
    n = 1
    while n < len(my_list):
        sort_flag = True  # небольшая доработка - флаг перестановок
        for i in range(len(my_list) - n):
            if my_list[i] < my_list[i + 1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
                sort_flag = False
        if sort_flag:  # если не было не одно перестановки то дальше можно не продолжать
            break
        n += 1
    return my_list


sample_list = [random.randint(-100, 100) for i in range(20)]
print('первоначальный список : ', sample_list)
my_sort(sample_list)
print('отсортированый список : ', sample_list)
