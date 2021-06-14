"""В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9."""

result = []
for i in range(2, 10):
    for j in range(i, 100, i):
        result.append(j)
print(len(result))
