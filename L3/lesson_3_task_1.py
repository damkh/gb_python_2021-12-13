# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
# пользователя, предусмотреть обработку ситуации деления на ноль.

# Функция, которая считает частное
def calc_division(dividend, divisor):
    try:
        return dividend / divisor
    except ZeroDivisionError:
        print('На 0 делить нельзя')


while True:
    try:
        a = float(input('Введите делимое a: '))
        break
    except ValueError:
        print("Должно быть число")

while True:
    try:
        b = float(input('Введите делитель b: '))
        break
    except ValueError:
        print("Должно быть число")

print(f'Результат деления a/b: {calc_division(a, b)}')
