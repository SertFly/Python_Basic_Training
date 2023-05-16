print('Задача 2. Соседи')


# Дана строка S и номер позиции символа в строке. Напишите программу, которая
# выводит соседей этого символа и сообщение о количестве таких же символов среди
# этих соседей: их нет, есть ровно один или есть два таких же.

def symbol_finder(symbols, number):
    sym_list = list(symbols)
    sym = sym_list[number - 1]
    sym_left = sym_list[number - 2]
    sym_right = sym_list[number]

    print('Символ слева:', sym_left)
    print('Символ справа:', sym_right)

    if sym == sym_left == sym_right:
        print('Два таких же символа!')
    elif sym == sym_left or sym == sym_right:
        print('Один такой же символ.')
    else:
        print('Похожих символов нет...')


while True:
    symbols = input('\nВведите строку: ')
    number = int(input('Введите номер символа: '))
    symbol_finder(symbols, number)
