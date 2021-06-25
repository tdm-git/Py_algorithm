"""
Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
коллекция, элементы которой это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
import collections
# для удобства работы зададим словарь прямого и обратного преобразования 16<>10 системы счисления
hex_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
            0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}


def sum_hex(a: str, b: str):  # на входе получаем строковые переменные
    result = collections.deque()  # результат вычисления
    transfer = 0
    if len(a) > len(b):  # для однозначности первая переменная будет большее по длине число
        a, b = collections.deque(a), collections.deque(b)
    else:
        a, b = collections.deque(b), collections.deque(a)
    while a:  # двигаемся по числу и вычисляем поэлементный результат
        if b:
            res = hex_dict[a.pop()] + hex_dict[b.pop()] + transfer  # результат считаем в 10-й системе
        else:
            res = hex_dict[a.pop()] + transfer
        result.appendleft(hex_dict[res % 16])  # в результирующий список переводим обратно в 16-ю
        transfer = res // 16  # переполнение разряда
    if transfer:
        result.appendleft(str(transfer))
    return result


def mult_hex(a: str, b: str):
    result = collections.deque()  # результат вычисления
    if len(a) > len(b):
        a, b = collections.deque(a), collections.deque(b)
    else:
        a, b = collections.deque(b), collections.deque(a)
    step = 0  # смещение числа, для сложения промежуточных результатов уумножения
    while b:  # в этом случае наоборот будем двигаться по кратчайшему из чисел
        b_next = hex_dict[b.pop()]  # получаем значение в 10-й системе
        a_copy = a.copy()  # кешируем второе число, т.к. для каждого прохода будем его "разбирать"
        transfer = 0  # начальное значение
        b_res = collections.deque()  # будем хранитьп ромежуточный результат
        while a_copy:
            res = (hex_dict[a_copy.pop()] * b_next) + transfer  # переменожаем в 10-й системе + переполнение
            b_res.appendleft(hex_dict[res % 16])  # собираем промежуточный результат
            transfer = res // 16
        if transfer:
            b_res.appendleft(str(transfer))
        for _ in range(step):  # проводим смещение промежуточного результата
            b_res.append('0')
        # для этого используем определенную функцию сложения, но необходимо список преобразовать в строку
        result = sum_hex("".join(result), "".join(list(b_res)))  # суммируем промежуточный результат с общим
        step += 1
    return result

user1 = 'A2'
user2 = 'C4F'
# user1 = input('введите первое число - ').upper()
# user2 = input('введите второе число - ').upper()
print(f'{user1} + {user2} = ', "".join(sum_hex(user1, user2)))
print(f'{user1} * {user2} = ', "".join(mult_hex(user1, user2)))
