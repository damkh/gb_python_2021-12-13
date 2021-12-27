"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""

import random


def gen_matrix_of_random(f_matrix_columns_quantity, f_matrix_rows_quantity):
    matr = []
    for raw_idx in range(0, f_matrix_rows_quantity):
        a_raw = []
        for column_idx in range(0, f_matrix_columns_quantity):
            a_raw.append(random.randint(min_val, max_val))
        matr.append(a_raw)
    return matr


class Matrix:
    def __init__(self, matrix, start=0):
        self.matrix = matrix
        self.i = start - 1

    def __add__(self, other):
        res_matrix = []
        if self.check_dimension(other):
            for (row_1, row_2) in zip(self.matrix, other.matrix):
                res_matrix_row = []
                for (elem_1, elem_2) in zip(row_1, row_2):
                    res_matrix_row.append(elem_1 + elem_2)
                res_matrix.append(res_matrix_row)
        return Matrix(res_matrix)

    def __str__(self):
        str_column = ''
        for row in self.matrix:
            str_row = ''
            for elem in row:
                str_row += f'{elem}\t'
            str_column += f'{str_row}\n'
        return str_column

    def check_dimension(self, other):
        return self.get_dimension() == other.get_dimension()

    def get_dimension(self):
        row_num = len(self.matrix)
        if row_num == 0:
            return 0
        else:
            column_num = len(self.matrix[0])
            if column_num == 0:
                return 0
            else:
                return row_num, column_num


matrix_columns_quantity = 2
matrix_rows_quantity = 2
min_val = -5
max_val = 10

# Генерация данных в матрице рандомно
a_matrix_1 = gen_matrix_of_random(matrix_columns_quantity, matrix_rows_quantity)
a_matrix_2 = gen_matrix_of_random(matrix_columns_quantity, matrix_rows_quantity)
a_matrix_3 = gen_matrix_of_random(matrix_columns_quantity, matrix_rows_quantity)
print(f'Matrix 1 - RAW SOURCE:\n{a_matrix_1}')
print(f'Matrix 2 - RAW SOURCE:\n{a_matrix_2}')
print(f'Matrix 3 - RAW SOURCE:\n{a_matrix_3}')
my_matrix_1 = Matrix(a_matrix_1)
my_matrix_2 = Matrix(a_matrix_2)
my_matrix_3 = Matrix(a_matrix_3)
print(f'Matrix 1 - Привычный вид:\n{my_matrix_1}')
print(f'Matrix 2 - Привычный вид:\n{my_matrix_2}')
print(f'Matrix 3 - Привычный вид:\n{my_matrix_3}')
print(f'Matrix 1+2:\n{my_matrix_1 + my_matrix_2}')
print(f'Matrix 1+2+3:\n{my_matrix_1 + my_matrix_2 + my_matrix_3}')
