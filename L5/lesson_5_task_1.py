# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об
# окончании ввода данных свидетельствует пустая строка.


with open('file_5_1.txt', 'w', encoding='utf-8') as file_obj:
    while True:
        in_str = input('Введите что-нибудь: ')
        if in_str:
            file_obj.write(in_str + '\n')
        else:
            break
