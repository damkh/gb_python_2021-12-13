# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.


salary = 20000

with open('file_5_3.txt', 'r', encoding='utf-8') as file_obj:
    content = file_obj.read()

    next_employee = (employee.split() for employee in content.splitlines() if int(employee.split()[1]) < salary)
    employee_quantity = 0
    salary_sum = 0
    while True:
        try:
            relevant_employee = next(next_employee)
            print(f'{relevant_employee[0]} с зарплатой {relevant_employee[1]}')
            employee_quantity += 1
            salary_sum += int(relevant_employee[1])
        except StopIteration:
            print(f'Сотрудников с зарплатой менее {salary}: {employee_quantity}')
            print(f'Средняя величина дохода этих сотрудников: {salary_sum}/{employee_quantity} = {salary_sum / employee_quantity}')
            break
