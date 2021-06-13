"""7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
1+2+...+n = n(n+1)/2, где n - любое натуральное число."""

user_input = int(input('введите количество элементов - '))
result1 = 0
result2 = 0
for i in range(user_input + 1):
    result1 += i
result2 = user_input*(user_input + 1) / 2
print(result1)
print(result2)
