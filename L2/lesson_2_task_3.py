# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима,
# весна, лето, осень). Напишите решения через list и через dict.

while True:
    try:
        month = int(input('Enter month number: '))
        if 1 <= month <= 12:
            break
        else:
            print('Month number is out of range [1; 12]')
    except ValueError:
        print('Month should be number in the range [1; 12]')

month_season_list = ['winter', 'spring', 'summer', 'autumn']

# DICT
month_season_dict = {
    1: month_season_list[0],
    2: month_season_list[0],
    3: month_season_list[1],
    4: month_season_list[1],
    5: month_season_list[1],
    6: month_season_list[2],
    7: month_season_list[2],
    8: month_season_list[2],
    9: month_season_list[3],
    10: month_season_list[3],
    11: month_season_list[3],
    12: month_season_list[0],
}
print(f'DICT: The season of month {month} is: \033[1m{month_season_dict[month].title()}\033[0m')

# LIST
print(f'LIST: The season of month {month} is: \033[1m{month_season_list[(month - 12) // 3].title()}\033[0m')
