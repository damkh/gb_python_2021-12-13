# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если слово длинное, выводить только первые 10 букв в слове.

# sentence = 'asd e23 sdf efwef 2f2 1234567890123'
sentence = input('Enter string: ')
for index, elem in enumerate(sentence.split()):
    print(f'{index + 1}) {elem[:10]}')
