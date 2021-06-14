"""9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр."""

user_input = input('введите последовательность элементов - ')
max_ch = 0
max_sum = 0
for i in user_input.split():
    ch_sum = 0
    for j in str(i):
        ch_sum += int(j)
    if max_sum < ch_sum:
        max_sum = ch_sum
        max_ch = i
print(f'в введенной последовательности - число с максимальной суммой цифр {max_ch} , сумма цифр которого {max_sum}')



