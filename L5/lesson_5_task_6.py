# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
# лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого
# предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее
# количество занятий по нему. Вывести словарь на экран.
#
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

with open('file_5_6.txt', 'r', encoding='utf-8') as file_obj:
    content = file_obj.read()
    lessons = (a_lesson for a_lesson in content.splitlines())
    lessons_dict = dict()
    while True:
        try:
            a_lesson = next(lessons)
            print(a_lesson)
            lec_num, pract_num, lab_num = 0, 0, 0
            try:
                lec_num = int(a_lesson.split()[1].split('(')[0])
            except ValueError:
                pass
            try:
                pract_num = int(a_lesson.split()[2].split('(')[0])
            except ValueError:
                pass
            try:
                lab_num = int(a_lesson.split()[3].split('(')[0])
            except ValueError:
                pass
            total_les_num = lec_num + pract_num + lab_num
            lessons_dict[a_lesson.split(':')[0]] = total_les_num

        except StopIteration:
            break
print(f'Словарь: \n{lessons_dict}')
