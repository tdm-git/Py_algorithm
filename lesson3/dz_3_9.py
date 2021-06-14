"""Найти максимальный элемент среди минимальных элементов столбцов матрицы"""
sample_matrix = [[2, 3, 4, 1], [4, 2, 3, 6], [6, 4, 2, 3], [4, 9, 2, 3]]
min_line = []

for i in zip(*sample_matrix):
    min_ch = i[0]
    for j in i:
        if j < min_ch:
            min_ch = j
    min_line.append(min_ch)

max_ch = min_line[0]
for i in min_line:
    if max_ch < i:
        max_ch = i

print(min_line)
print(max_ch)
