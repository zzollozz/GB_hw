a=0
""" Осуществить программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс «Клетка».
    В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). 
    В классе должны быть реализованы методы перегрузки арифметических операторов:
     сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__floordiv____truediv__()).
    Эти методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и округление до целого числа
    деления клеток соответственно."""

class Cell:
    def __init__(self, param):
        self.param = param

    def __add__(self, other):
        return self.param + other.param

    def __sub__(self, other):
        if self.param - other.param > 0:
            return self.param - other.param
        else:
            return f'Разница ячеек клеток {self.param} и {other.param} меньше 0'

    def __mul__(self, other):
        return self.param * other.param

    def __floordiv__(self, other):
        return self.param // other.param



cletka_a = Cell(150)
cletka_b = Cell(23)

print(cletka_a // cletka_b)
