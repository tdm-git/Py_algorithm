"""В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать."""
import random

sample_list = [random.randint(1, 100) for i in range(15)]
max_ind = 0
min_ind = 0
max_ch = sample_list[0]
min_ch = sample_list[0]
for i, j in enumerate(sample_list):  # ищем max\min элементы и индексы
    if j > max_ch:
        max_ch = j
        max_ind = i
    if j < min_ch:
        min_ch = j
        min_ind = i
print('первоначальный список - ', sample_list)
print(f'максимальный элемент {max_ch}  (на {max_ind + 1} позиции); минимальный элемент {min_ch} (на {min_ind + 1} позиции)')
result = 0
if min_ind <= max_ind:
    for i in range(min_ind + 1, max_ind):
        result += sample_list[i]
else:
    for i in range(max_ind + 1, min_ind):
        result += sample_list[i]
print('1.сумма элементов между ними - ', result)
# второй вариант решения
result = 0
max_ind = sample_list.index(max(sample_list))
min_ind = sample_list.index(min(sample_list))
for i in range(min(min_ind, max_ind)+1, max(min_ind, max_ind)):
    result += sample_list[i]
print('2.сумма элементов между ними - ', result)
