# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text. Продолжить работу над заданием. В
# программу должна попадать строка из слов, разделенных пробелом. Каждое слово состоит из латинских букв в нижнем
# регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Необходимо
# использовать написанную ранее функцию int_func().

# Реализация через срезы
# def int_func(word):
#     return word[0].upper() + word[1:]

# Реализация через ASCII-коды
# def int_func(word):
#     return chr(int(ord(word[0])) - 32) + word[1:]

# Реализация через capitalize()
def int_func(word):
    return word.capitalize()


one_word = input('Введите слово: ')
print(int_func(one_word))

my_sentence = input('Введите предложение: ')

sentence_words = my_sentence.split()
print(' '.join(list(map(int_func, sentence_words))))
