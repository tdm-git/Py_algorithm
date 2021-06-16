"""В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию (индекс) в массиве."""
import random

sample_list = [random.randint(-100, 100) for i in range(15)]
max_ind = 0
max_ch = -100
for i, j in enumerate(sample_list):
    if 0 > j > max_ch:  # двойное условие - максимально среди минимальных
        max_ch = j
        max_ind = i
print('список - ', sample_list)
print(f'максимальное отрицательно число "{max_ch}" находится на {max_ind} позиции')
