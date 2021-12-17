# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и
# 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка
# элементов необходимо использовать функцию input().

lst = list()
while True:
    el = input(f"Введите элемент списка (для завершения ввода введите кодовое слово END): ")
    if el == 'END':
        break
    else:
        lst.append(el)
print(f'Полученный список: {lst}')

lst_new = list()
for first, second in zip(lst[::2], lst[1::2]):
    lst_new.extend([second, first])
if len(lst[::2]) != len(lst[1::2]):
    lst_new.append(lst[-1])
print(f'new list:\n{lst_new}')
