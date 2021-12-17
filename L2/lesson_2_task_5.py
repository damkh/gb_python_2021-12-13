# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя
# необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
#
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
my_list = [7, 5, 3, 3, 2]
print(f'Initial list: {my_list}')

new_elem = 5
while True:
    try:
        new_elem = input('Enter new element: ')
        new_elem_int = int(new_elem)
        if 1 <= new_elem_int == float(new_elem):
            break
        else:
            print('Element should be natural number')
    except ValueError:
        print('Element should be natural number')

position = 0
if my_list:
    while new_elem_int <= my_list[position]:
        position += 1
        if position == len(my_list):
            my_list.append(new_elem_int)
            break
    else:
        my_list.insert(position, new_elem_int)
else:
    my_list.append(new_elem_int)

print(f'Insert {new_elem_int} to postition {position}, result list:')
for index, elem in enumerate(my_list):
    if index == position:
        print(f'\033[1m{elem}\033[0m', end=' ')
    else:
        print(f'{elem}', end=' ')
