# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

with open('file_5_2.txt', 'r', encoding='utf-8') as file_obj:
    content = file_obj.read()

    # Подсчет количества строк
    print(f'Количество строк: {len(content.splitlines())}')

    # Подсчет количества слов в каждой строке
    for num, a_line in enumerate(content.splitlines()):
        print(f'Количество слов в строке "{a_line}" = {len(a_line.split())}')
