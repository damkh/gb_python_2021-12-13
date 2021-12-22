# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа
# должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint

max_num_quantity = 5
min_num_value = 0
max_num_value = 10
with open('file_5_5.txt', 'w', encoding='utf-8') as file_obj:
    for quantity in range(max_num_quantity):
        file_obj.write(f'{randint(min_num_value, max_num_value)} ')

with open('file_5_5.txt', 'r', encoding='utf-8') as file_obj:
    content = file_obj.readline()
    print(f'Содержимое файла {file_obj.name}: {content}')
    num_sum = 0
    for num in content.split():
        try:
            num_sum += float(num)
        except ValueError:
            print(f'"{num}" - не число, оно не будет учитываться в сумме')
    print(f'Сумма всех чисел: {num_sum}')
