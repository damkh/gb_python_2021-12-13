"""
7.  Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
    реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
    создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
    Проверьте корректность полученного результата.
"""


class ComplexNumber:
    def __init__(self, real_part, im_part):
        self.real_part = real_part
        self.im_part = im_part

    def __add__(self, other):
        return ComplexNumber(self.real_part + other.real_part, self.im_part + other.im_part)

    def __sub__(self, other):
        return ComplexNumber(self.real_part - other.real_part, self.im_part - other.im_part)

    def __mul__(self, other):
        return ComplexNumber(self.real_part * other.real_part - self.im_part * other.im_part,
                             self.real_part * other.im_part + other.real_part * self.im_part)

    def __truediv__(self, other):
        if not other.check_if_zero():
            common_denom = other.real_part ** 2 + other.im_part ** 2
            re_p = (self.real_part * other.real_part + self.im_part * other.im_part) / common_denom
            im_p = (-self.real_part * other.im_part + other.real_part * self.im_part) / common_denom
            return ComplexNumber(re_p, im_p)
        else:
            print('Деление на 0')

    def check_if_zero(self):
        if self.real_part == 0 and self.im_part == 0:
            return True

    def __str__(self):
        return f'{self.print_re_part}' + f'{self.print_im_part}'

    @property
    def print_re_part(self):
        return f'{self.real_part}'

    @property
    def print_im_part(self):
        if self.im_part > 0:
            if self.im_part != 1:
                return f' + {self.im_part}i'
            else:
                return f' + i'
        elif self.im_part < 0:
            return f' - {-self.im_part}i'
        else:
            return f' '


a1 = ComplexNumber(0, 2)
a2 = ComplexNumber(-2, 1)
print(f'a1 = {a1}')
print(f'a2 = {a2}')
a3 = a1 + a2
print(f'a1 + a2 = {a3}')
a4 = a1 - a2
print(f'a1 - a2 = {a4}')
a5 = a1 * a2
print(f'a1 * a2 = {a5}')
a6 = a1 / a2
print(f'a1 / a2 = {a6}')


