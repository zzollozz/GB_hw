""" 4. Написать декоратор с аргументом-функцией (callback),
       позволяющий валидировать входные значения функции и выбрасывать исключение ValueError """

def val_checker(callback):
    def my_func(func):
        def wrepper(*args, **kwargs):
            for el in args:
                if not callback(el):
                    raise ValueError(f'wrong val {el}')
                else:
                    return func(*args, **kwargs)
        return wrepper
    return my_func





@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


# print(calc_cube(5))
#   125

print(calc_cube(-5))
#   ValueError: wrong val -5


####################################################################################

