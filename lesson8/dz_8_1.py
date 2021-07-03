"""Определить количество различных подстрок с использованием хеш-функции. Задача: на вход функции дана строка,
требуется вернуть количество различных подстрок в этой строке. 
Примечание: в сумму не включаем пустую строку и строку целиком."""
import hashlib


user_input = input('введите строку - ')
sum_substring = set()  # используем множество для получения уникальных значений
for i in range(len(user_input)):
    for j in range(len(user_input), i, -1):
        sub_str = user_input[i:j]
        if sub_str == user_input or sub_str.isspace():  # исключим по условию из примечания задачи
            continue
        # sum_substring.add(sub_str)
        sum_substring.add(hashlib.sha1(sub_str.encode('utf-8')).hexdigest())
# print(sum_substring)
print(f'в строке "{user_input}" - встречается {len(sum_substring)} подстроки')
