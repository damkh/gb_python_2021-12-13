# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

a = float(input("Введите результат в 1-й день (км): "))
b = float(input("Введите результат в искомый день (км): "))

results = list()
results.append(a)

while True:
    if a >= b:
        break
    a *= 1.1
    results.append(a)

for day, res in enumerate(results):
    print(f'{day + 1}-й день: {round(res, 2)}')

print(f'На {len(results)}-й день спортсмен достиг результата — не менее {b} км.')
