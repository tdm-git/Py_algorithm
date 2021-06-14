"""В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
(оба являться минимальными), так и различаться."""
import random

sample_list = [random.randint(1, 100) for i in range(15)]
min1 = sample_list[0]
min2 = sample_list[1]
for i in sample_list:
    if i < min1:
        min1 = i
        if min1 < min2:
            min2, min1 = min1, min2
print(sample_list)
print(min1, min2)
