"""9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр."""

user_input = input('введите последовательность элементов - ')
max_ch = 0
max_sum = 0
for i in user_input.split():
    if max_ch < int(i):
        max_ch = int(i)
for i in str(max_ch):
    max_sum += int(i)
print(f' {max_ch} {max_sum}')



