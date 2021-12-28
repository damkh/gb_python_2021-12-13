"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя
программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class MyZeroDivError(Exception):
    def __init__(self, message):
        self.message = message


a = 10
b = 0
try:
    if b == 0:
        raise MyZeroDivError('b не может равняться 0')
    else:
        result = a/b
except TypeError:
    print('Возможно вы ввели не числа')
except MyZeroDivError as e:
    print(e)
else:
    print(f'a/b = {result}')
