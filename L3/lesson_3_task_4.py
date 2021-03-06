# 4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить
# возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания
# необходимо обойтись без встроенной функции возведения числа в степень.
#
# ** Подсказка:** попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def my_func(x, y):
    s = x
    for i in range(1, -y):
        s *= x
    return f'Через цикл: {1 / s}, через встроенный оператор: {x ** y}'


while True:
    try:
        x = float(input('Введите действительное положительное число x: '))
        if x > 0:
            break
        else:
            print("Должно быть действительное положительное число")
    except ValueError:
        print("Должно быть действительное положительное число")

while True:
    try:
        y = int(input('Введите целое отрицательное число y: '))
        if y < 0:
            break
        else:
            print("Должно быть целое отрицательное число")
    except ValueError:
        print("Должно быть целое отрицательное число")

print(my_func(x, y))