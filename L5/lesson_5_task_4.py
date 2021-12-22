# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

rus_numerals = {
    '0': 'ноль',
    '1': 'один',
    '2': 'два',
    '3': 'три',
    '4': 'четыре',
    '5': 'пять',
    '6': 'шесть',
    '7': 'семь',
    '8': 'восемь',
    '9': 'девять'
}

with open('file_5_4_en.txt', 'r', encoding='utf-8') as file_obj:
    content = file_obj.read()
    english_numerals = (a_numeral for a_numeral in content.splitlines())

with open('file_5_4_rus.txt', 'w', encoding='utf-8') as file_obj:
    while True:
        try:
            num = next(english_numerals).split(" — ")[1]
            file_obj.write(f'{rus_numerals[num]} — {num}\n')
        except StopIteration:
            break
