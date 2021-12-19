# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
# аргументов.

def my_func(a, b, c):
    if a <= b and a <= c:
        return b + c
    elif b <= c and b <= a:
        return a + c
    else:
        return a + b


first = 7
second = 5
third = 3

# first = float(input('Enter first number: '))
# second = float(input('Enter second number: '))
# third = float(input('Enter third number: '))

print(first, second, third)
print(my_func(first, second, third))

