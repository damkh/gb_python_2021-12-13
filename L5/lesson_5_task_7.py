# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные
# о фирме: название, форма собственности, выручка, издержки.
#
# Пример строки файла: firm_1 ООО 10000 5000. Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать. Далее реализовать
# список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма
# получила убытки, также добавить ее в словарь (со значением убытков).
#
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json


def to_json(obj, file_name='file_5_7.json'):
    with open(file_name, 'w') as json_obj:
        json.dump(obj, json_obj)
        print(f'Сохранено в файл {file_name}')


with open('file_5_7.txt', 'r', encoding='utf-8') as file_obj:
    content = file_obj.read()
    companies = (a_company for a_company in content.splitlines())
    profit_list = list()
    profit_dict = {'Тип': 'Прибыль'}
    loss_dict = {'Тип': 'Убыток'}
    average_profit_dict = dict()
    average_profit = 0
    profit_sum = 0
    company_num = 0
    while True:
        try:
            a_company = next(companies)
            print(a_company)
            try:
                company_revenue = float(a_company.split()[2])
            except ValueError:
                pass
            try:
                company_cost = float(a_company.split()[3])
            except ValueError:
                pass

            company_profit = company_revenue - company_cost
            if company_profit >= 0:
                company_num += 1
                profit_sum += company_profit
                profit_dict.update({f'{a_company.split()[1]} {a_company.split()[0]}': company_profit})
            else:
                loss_dict.update({f'{a_company.split()[1]} {a_company.split()[0]}': -company_profit})
        except StopIteration:
            break
average_profit = profit_sum / company_num
average_profit_dict.update({"Средняя прибыль": average_profit})
profit_list.append(profit_dict)
profit_list.append(average_profit_dict)
profit_list.append(loss_dict)
print(profit_list)
to_json(profit_list)


