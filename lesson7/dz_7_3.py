"""Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой
называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.
Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках."""
import random


def list_mediana(lst: list, first: int, last: int):  # рекурсивная функция поиска медианы
    ind = len(lst) // 2
    if first >= last:  # условие выхода из рекурсии
        return lst[ind]
    splitter = lst[ind]  # значение середины списка
    i = first
    j = last
    while i <= j:
        while lst[i] < splitter:  # проверяем значения слева от разделителя
            i += 1
        while lst[j] > splitter:  # проверяем значения справа от разделителя
            j -= 1
        if i <= j:  # делаем перестановку
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
            j -= 1
    if ind < i:  # если не совпали то рекурсивно повторяем поиск
        lst[ind] = list_mediana(lst, first, j)
    elif j < ind:
        lst[ind] = list_mediana(lst, i, last)
    return lst[ind]  # иначе возвращаем значение


m = 3
sample_list = [random.randint(0, 50) for i in range(2 * m + 1)]
print('первоначальный список: ', sample_list)
print('медианное значение: ', list_mediana(sample_list, 0, len(sample_list) - 1))
