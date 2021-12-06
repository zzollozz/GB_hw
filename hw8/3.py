"""
3. Написать декоратор для логирования типов позиционных аргументов функции,
например:

Примечание:
     если аргументов несколько - выводить данные о каждом через запятую;
     можете ли вы вывести тип значения функции? Сможете ли решить задачу для именованных аргументов?
     Сможете ли вы замаскировать работу декоратора? Сможете ли вывести имя функции, например, в виде:
"""

def type_logger(func):
    def wrapper(*args, **kwargs):
            # print({' '.join(f'{i}: {type(i)}' for i in args)})     #  Первый вариант
            print(f"{func.__name__} ({' '.join(f'{i}: {type(i)}' for i in args)})")  # Второй вариант
            return func(*args, **kwargs)
    return wrapper



@type_logger
def calc_cube(x, a, b, c):
    return x ** 3


calc_cube(5)
# 5, <class 'int'>

calc_cube(5, 'Hello Word', 23.32, -23)
#5: <class 'int'> Hello Word: <class 'str'> 23.32: <class 'float'> -23: <class 'int'>


calc_cube(5)
# calc_cube (5: <class 'int'>)