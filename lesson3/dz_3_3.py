"""В массиве случайных целых чисел поменять местами минимальный и максимальный элементы."""
import random

list1 = [random.randint(1, 100) for i in range(10)]
max_ind = 0
max_ch = list1[0]
min_ind = 0
min_ch = list1[0]
for i, j in enumerate(list1):  # найдем максимальный и минимальный элемент и их индексы
    if j > max_ch:
        max_ch = j
        max_ind = i
    if j < min_ch:
        min_ch = j
        min_ind = i
print('первоначальный список - ', list1)
print(f'максимальный элемент {max_ch}  ; минимальный элемент {min_ch} ')
# синтаксис Python позволяет сделать замену в одной строке
list1[max_ind], list1[min_ind] = list1[min_ind], list1[max_ind]
print('отредактированный список - ', list1)
print('*' * 100)
# второй вариант с использованием min и max
list2 = [random.randint(1, 100) for i in range(10)]  # генерируем новый список
print('первоначальный список - ', list2)
max_ind = list2.index(max(list2))  # получим индексы элементов и сделаем замену
min_ind = list2.index(min(list2))  # если число встречается неоднократно то в качестве индекса будет первое вхождение
print(f'максимальный элемент {list2[max_ind]}  ; минимальный элемент {list2[min_ind]} ')
list2[max_ind], list2[min_ind] = list2[min_ind], list2[max_ind]
print('отредактированный список - ', list2)
