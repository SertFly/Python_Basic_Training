sym_sum = 0
line_count = 0
try:
    people_file = open('people.txt', 'r', encoding='utf-8')
    for i_line in people_file:
        length = len(i_line)
        line_count += 1
        if i_line.endswith('\n'):
            length -= 1
        if 0 < length < 3:
            raise BaseException('Длина {} строки менее 3-х символов'.format(line_count))
        sym_sum += length
    people_file.close()

except FileNotFoundError:
    print('Файл с именами не найден.')
finally:
    print('Количество найденных символов:', sym_sum)
