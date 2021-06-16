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
print(f'максимальный элемент {max_ch}  (на {max_ind} позиции); минимальный элемент {min_ch} (на {min_ind} позиции)')
result = 0
for i in range(min(min_ind, max_ind)+1, max(min_ind, max_ind)):  # решил использовать max\min
    print(sample_list[i])
    result += sample_list[i]                                     # можно было использовать отрицательный шаг range
print('сумма элементов между ними - ', result)
# второй вариант решения
# result = 0
# max_ind = sample_list.index(max(sample_list))
# min_ind = sample_list.index(min(sample_list))
# step = 1 if min_ind <= max_ind else -1  # используем тернарный оператор
# for i in range(min_ind + (1 + step), max_ind + (1 - step), step):
#     print(sample_list[i])
#     result += sample_list[i]
# print('сумма элементов между ними - ', result)
