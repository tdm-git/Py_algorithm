"""Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке
 [0; 50). Выведите на экран исходный и отсортированный массивы."""
import random


def my_sort(my_list):

    def merge(fst, snd):  # функция сортировки слиянием
        res = []
        i, j = 0, 0
        while i < len(fst) and j < len(snd):
            if fst[i] < snd[j]:
                res.append(fst[i])
                i += 1
            else:
                res.append(snd[j])
                j += 1
        res.extend(fst[i:] if i < len(fst) else snd[j:])
        return res

    def div_half(lst):  # рекурсивная функция разбиения массива
        if len(lst) == 1:
            return lst
        elif len(lst) == 2:
            return lst if lst[0] <= lst[1] else lst[::-1]
        else:
            return merge(div_half(lst[:len(lst) // 2]), div_half(lst[len(lst) // 2:]))

    return div_half(my_list)


sample_list = [random.randint(0, 50) for i in range(20)]
print('первоначальный список : ', sample_list)
print('отсортированый список : ', my_sort(sample_list))
