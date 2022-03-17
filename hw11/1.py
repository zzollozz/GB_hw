""" 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
    В рамках класса реализовать два метода. Первый, с декоратором @classmethod. 
    Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
    Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
    Проверить работу полученной структуры на реальных данных """
from datetime import datetime


class Date:
    def __init__(self, param):
        self.param = param

    @classmethod
    def date_int(cls, param):
        date_int = [int(i) for i in param.split('-')]
        return date_int

    @staticmethod
    def valid_date(self):
        try:
            if datetime.strptime(self.param, "%d-%m-%Y"):
                print(True)
        except ValueError as e:
            print(f'Дата {self.param} не валидна')
            print(e)


print(Date.date_int('23-05-1978'))

Date.valid_date(Date('23-05-1978'))





