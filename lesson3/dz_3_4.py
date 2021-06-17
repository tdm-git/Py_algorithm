"""Определить, какое число в массиве встречается чаще всего."""
import random
# поскольку справочники будут на следующем занятии, решим задачу с помошью списков
sample_list = [random.randint(1, 10) for i in range(15)]
list1 = []  # используем список для уникальных значений
list2 = []  # синхронизированный список для количества элементов
for i in sample_list:
    if i in list1:
        list2[list1.index(i)] += 1  # увеличиваем счетчик на 1
    else:
        list1.append(i)  # если такого элемента нет добавляем значение и счетчик
        list2.append(1)
max_ind = 0
max_ch = list2[0]
for i, j in enumerate(list2):
    if j > max_ch:
        max_ch = j
        max_ind = i
print('список - ', sample_list)
# print(list1, list2)
# при одинаковом количестве повторов нескольких чисел - будет выведено первое с таким количеством
print(f'число "{list1[max_ind]}" встречается чаще всех - {max_ch} раз')
