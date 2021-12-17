# 6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит
# информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно,
# т.е. запрашивать все данные у пользователя.
#
# Пример готовой структуры:
# [
#     (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#     (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#     (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
#
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.
#
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

# Для быстрой проверки
# products = [
#     (1, {"название": "компьютер", "цена": 20000, "количество": 5, "ед": "шт."}),
#     (2, {"название": "принтер", "цена": 6000, "количество": 2, "ед": "шт."}),
#     (3, {"название": "сканер", "цена": 2000, "количество": 7, "ед": "шт."}),
#     (4, {"название": "картошка", "цена": 20, "количество": 12, "ед": "кг"}),
#     (5, {"название": "уборка", "цена": 200, "количество": 1, "ед": "усл."})
# ]

# Заполнение товаров вручную
products = list()
idx = 1
product_keys = ['название', 'цена', 'количество', 'ед']
while True:
    product_dict = dict()
    for param in product_keys:
        if param == 'цена':
            # Цена
            while True:
                product_param = input(f'Введите значение поля "{param}": ')
                if product_param:
                    try:
                        product_param = float(product_param)
                        product_dict.update({param: product_param})
                        break
                    except ValueError:
                        print(f'{param} должна быть числом')
                else:
                    print(f'Поле не должно быть пустым')
        elif param == 'количество':
            # Количество
            while True:
                product_param = input(f'Введите значение поля "{param}": ')
                if product_param:
                    try:
                        product_param = int(product_param)
                        product_dict.update({param: product_param})
                        break
                    except ValueError:
                        print(f'{param} должно быть ЦЕЛЫМ числом')
                else:
                    print(f'Поле не должно быть пустым')
        else:
            while True:
                product_param = input(f'Введите значение поля "{param}": ')
                if product_param:
                    product_dict.update({param: product_param})
                    break
                else:
                    print(f'Поле не должно быть пустым')

    products.append((idx, product_dict))
    idx += 1
    if input('Введите "Y" для добавления еще одного товара, иначе оставьте поле пустым и нажмите Enter. ') != 'Y':
        break

print('Список товаров: [')
for el in products:
    print(el)
print(']')

products_analysed = dict()

for product_key in product_keys:
    key_values = []
    for product in products:
        key_values.append(product[1].get(product_key))
    key_values = list(set(key_values))
    products_analysed.update({product_key: key_values})

print('Результат: ')
print('{')
for key in products_analysed:
    print(f'\t\'{key}\': {products_analysed[key]}')
print('}')
