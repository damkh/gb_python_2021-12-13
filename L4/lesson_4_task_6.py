# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не
# должен быть бесконечным. Необходимо предусмотреть условие его завершения. Например, в первом задании выводим целые
# числа, начиная с 3, а при достижении числа 10 завершаем цикл. Во втором также необходимо предусмотреть условие,
# при котором повторение элементов списка будет прекращено.

from itertools import count
from itertools import cycle

# a
start_num = 3
end_num = 10
print(f'Скрипт А: целые числа, с {start_num} до {end_num}')
for el in count(start_num):
    if el > end_num:
        break
    else:
        print(el, end=' ')

# b
init_list = [1, 3, 4]
cycle_max = 5
cycle_num = 1
print(f'\nСкрипт Б: повторение элементов списка {init_list} {cycle_max} раз')

for el in cycle(init_list):
    if cycle_num > cycle_max * len(init_list):
        break
    else:
        print(el, end=' ')
    cycle_num += 1
