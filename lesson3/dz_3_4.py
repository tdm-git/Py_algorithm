"""Определить, какое число в массиве встречается чаще всего."""
import random

sample_list = [random.randint(1, 10) for i in range(15)]
list1 = []
list2 = []
for i in sample_list:
    if i in list1:
        list2[list1.index(i)] += 1
    else:
        list1.append(i)
        list2.append(1)
max_ind = 0
max_ch = list2[0]
for i, j in enumerate(list2):
    if j > max_ch:
        max_ch = j
        max_ind = i
print(sample_list)
print(list1)
print(list2)
print(max_ch, list1[max_ind])
