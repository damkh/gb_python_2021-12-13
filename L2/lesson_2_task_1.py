# 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных
# каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у
# пользователя, а указать явно, в программе.

my_list = [1, 2.2, -3, 'string', True, (3 + 2j), ['a', 'b', 4, 3.3], ('c', 'd', 7, 8.8), {'set', 1, 5.5, 5.5},
           {'a1': 'b1', 'a2': 'b2'}, b'123', None, '1/0', 'math.sqrt(-2)']

for el in my_list:
    if type(el) == int:
        print(f'{el} - is \033[1minteger\033[0m')
        continue
    elif type(el) == float:
        print(f'{el} - is \033[1mfloat\033[0m')
        continue
    elif type(el) == str:
        print(f'{el} - is \033[1mstring\033[0m')
        continue
    elif type(el) == bool:
        print(f'{el} - is \033[1mbool\033[0m')
        continue
    elif type(el) == complex:
        print(f'{el} - is \033[1mcomplex\033[0m')
        continue
    elif type(el) == list:
        print(f'{el} - is \033[1mlist\033[0m')
        continue
    elif type(el) == tuple:
        print(f'{el} - is \033[1mtuple\033[0m')
        continue
    elif type(el) == dict:
        print(f'{el} - is \033[1mdict\033[0m')
        continue
    elif type(el) == set:
        print(f'{el} - is \033[1mset\033[0m')
        continue
    elif type(el) == bytes:
        print(f'{el} - is \033[1mbytes\033[0m')
        continue
    elif el is None:
        print(f'{el} - is \033[1mNone\033[0m')
    else:
        print(f'{el} : {type(el)}\033[1m - I don\'t know what is it \033[0m')
