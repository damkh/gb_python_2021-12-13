# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
# необходимо использовать формулу: (выработка в часах*ставка в час) + премия. Для выполнения расчета для конкретных
# значений необходимо запускать скрипт с параметрами.

from sys import argv


def calc_salary(f_work_hours, f_hourly_rate, f_bonus):
    salary = int(f_work_hours) * int(f_hourly_rate) + int(f_bonus)
    print(f'Зарплата: {salary}')


# параметрами по умолчанию
work_hours = 5
hourly_rate = 2
bonus = 3

if len(argv) == 1:  # Вычисление с параметрами по умолчанию
    print(f'Вычисление с параметрами по умолчанию: '
          f'выработка в часах = {work_hours}, ставка в час = {hourly_rate}, премия = {bonus}')
    calc_salary(work_hours, hourly_rate, bonus)
if len(argv) == 2:
    print('Недостаточно параметров')
elif len(argv) == 3:  # Без премии
    script_name, work_hours, hourly_rate = argv
    calc_salary(work_hours, hourly_rate, 0)
elif len(argv) == 4:  # С премией
    script_name, work_hours, hourly_rate, bonus = argv
    calc_salary(work_hours, hourly_rate, bonus)
elif len(argv) > 4:
    print('Есть лишние параметры')


