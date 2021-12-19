# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться
# сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь
# введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ,
# выполнение программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить
# сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def calc_process(number_list):
    numbers_sum = 0
    func_stop_symbol = False
    for number in number_list.split():
        if number == 'S':
            func_stop_symbol = True
            return numbers_sum, func_stop_symbol
        numbers_sum += float(number)
    return numbers_sum, func_stop_symbol


stop_symbol = False
glob_numbers_sum = 0
while not stop_symbol:
    my_number_list = input('Введите строку чисел, разделенных пробелом (Стоп-символ - S): ')
    calc_result = calc_process(my_number_list)
    stop_symbol = calc_result[1]
    glob_numbers_sum += calc_process(my_number_list)[0]
    print(glob_numbers_sum)

