# Представлен список чисел.Необходимо вывести те его элементы, значения которых больше
# предыдущего


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = []
for el in range(1, len(src)):
    if src[el] > src[el - 1]:
        result.append(src[el])
print(result)
