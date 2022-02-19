import random
""" 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
    который должен принимать данные (список списков) для формирования матрицы.
    Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
    Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix (двух матриц).
    Результатом сложения должна быть новая матрица."""
import numpy as np


class Matrix:
    def __init__(self, data_list):
        self.data_list = data_list

    def __str__(self):
        pass
        return '\n'.join(map(str, (self.data_list)))
        # return str(np.array(self.data_list))


    def __add__(self, other):
        new_data_list = []
        for i in range(len(self.data_list)):
            new_data_list.append([])
            for j in range(len(self.data_list[0])):
                new_data_list[i].append(self.data_list[i][j] + other.data_list[i][j])
        return '\n'.join(map(str, (new_data_list)))




if __name__ == '__main__':

    a = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
    b = [[4, 4, 4], [5, 5, 5], [6, 6, 6]]
    c = [[random.randint(10, 20) for x in range(3)] for y in range(3)]


    matrix_a = Matrix(a)
    matrix_b = Matrix(b)
    matrix_c = Matrix(c)

    print(matrix_a, '\n')
    # print(matrix_b, '\n')
    # print(matrix_a + matrix_b)
    print(matrix_a + matrix_c)

    matrix = np.array([[x for x in range(3)] for y in range(3)])
    matrix_1 = [[random.randint(10, 20) for x in range(3)] for y in range(3)]
    print(a, '\n')
    print(matrix, '\n')
    print(matrix_1, '\n')

