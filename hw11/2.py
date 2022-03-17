""" 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
    вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
    завершиться с ошибкой. """


class DivisionByZero:
    def __init__(self, param_1, param_2):
        self.divider = param_1
        self.denominator = param_2

    @staticmethod
    def divide_by_null(self):
        try:
            return self.divider / self.denominator
        except:
            return ("division by zero")



print(DivisionByZero.divide_by_null(DivisionByZero(10, 2)))
print(DivisionByZero.divide_by_null(DivisionByZero(10, 0)))
