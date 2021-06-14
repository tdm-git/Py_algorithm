"""В массиве случайных целых чисел поменять местами минимальный и максимальный элементы."""
import random

sample_list = [random.randint(1, 100) for i in range(15)]
max_ind = 0
min_ind = 0
max_ch = sample_list[0]
min_ch = sample_list[0]
for i, j in enumerate(sample_list):
    if j > max_ch:
        max_ch = j
        max_ind = i
    if j < min_ch:
        min_ch = j
        min_ind = i

print(sample_list)
print(max_ch, max_ind, min_ch, min_ind)
sample_list[max_ind], sample_list[min_ind] = sample_list[min_ind], sample_list[max_ind]
print(sample_list)
