print('Задача 1. Улучшенная лингвистика 2')

# Усовершенствуйте старую программу:

# У нас есть список из трёх слов, которые вводит пользователь. Затем вводится
# сам текст произведения, который вводится уже в одну строку. Напишите программу,
# которая посчитает, сколько раз слова пользователя встречаются в тексте.

check_wordlist = [input('Введите слово для анализа: ') for _ in range(3)]
text = input('Введите текст для анализа: ').split()

counter = [text.count(word) for word in check_wordlist]
print('\nРезультаты:')
print([str(check_wordlist[i]) + ' ' + str(counter[i]) for i in range(3)])


