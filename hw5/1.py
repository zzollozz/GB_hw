#   Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield,
"""Задание 1"""
def gen_odd(n):
    for i in range(1, n + 1, 2):
        yield i


# print(next(gen_odd(5)))  #--> Почему вот так нельзя записать почему не работает как положено Просто выводит результат
g = gen_odd(5)
# print(next(g))

"""Задание 2"""
def gen_namb(n):
    res = (el for el in range(1, n + 1) if el % 2 != 0)
    return res

h = gen_namb(6)
print(next(h))
