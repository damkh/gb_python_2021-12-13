# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

while True:
    n = int(input("Введите целое положительное число: "))
    if n > 0:
        break

digits = []
while True:
    ost = n % 10
    digits.append(int(ost))
    n = (n - ost) / 10
    if n == 0:
        break

maxel = 0
for i in digits:
    if i > maxel:
        maxel = i

print(maxel)

