# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего
# элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

import random

min_num = 0
max_num = 1000
num_quant = 10
# Начальный список рандомных чисел, сгененирован через генератор списка
src_list = [random.randint(min_num, max_num) for _ in range(num_quant)]
print(f'Начальный список: {src_list}')
# Создается генератор выражений на основе src_list.
src_list_gen = (num for num in src_list)

# 1 - Генератор нового списка (через индексы, но это не круто:))
dst_list_1 = [src_list[idx] for idx in range(1, len(src_list)) if src_list[idx] > src_list[idx - 1]]
print(f'Список через индексы: {dst_list_1}')

# 2 - Используя генератор
dst_list_2 = [a for a in src_list[1:] if a > next(src_list_gen)]
print(f'Список через генератор: {dst_list_2}')
