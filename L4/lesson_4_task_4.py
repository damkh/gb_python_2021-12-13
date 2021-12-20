# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел,
# соответствующих требованию. Элементы вывести в порядке их следования в исходном списке. Для выполнения задания
# обязательно использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

import random


min_num = 0
max_num = 10
num_quant = 10
# src_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
src_list = [random.randint(min_num, max_num) for num in range(num_quant)]
print(f'Начальный список: {src_list}')

# Новый список через генератор списков.
dst_list = [num for num in src_list if src_list.count(num) == 1]
print(f'Элементы списка, не имеющие повторений: {dst_list}')
