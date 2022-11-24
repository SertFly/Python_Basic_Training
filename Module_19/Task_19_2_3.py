print('Задача 3. Гистограмма частоты')


# Лингвистам нужно собрать данные о частоте букв в тексте, исходя из этих данных
# будет строиться гистограмма частоты букв.

# Напишите программу, которая получает сам текст и считает, сколько раз в строке
# встречается каждый символ. На экран нужно вывести содержимое в виде таблицы,
# отсортированное по алфавиту, а также максимальное значение частоты.


def histogram(text):
    hist_dict = {}
    for sym in text:
        if sym in hist_dict:
            hist_dict[sym] += 1
        else:
            hist_dict[sym] = 1
    return hist_dict


text = input('Введите текст: ').lower()
text_histogram = histogram(text)

for sym in sorted(text_histogram):
    print(sym, '-', text_histogram[sym])

print('Максимальное значение частоты:', max(text_histogram.values()))
