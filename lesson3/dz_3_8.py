"""Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа должна вычислять сумму
введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу."""
result = []
sum_ch = 0
line_list = []

for i in range(1, 17):
    user_choise = int(input('введите число - '))
    line_list.append(user_choise)
    sum_ch += user_choise
    if i % 4 == 0:
        line_list.append(sum_ch)
        result.append(line_list)
        sum_ch = 0
        line_list = []

for i in result:
    print(*i)
