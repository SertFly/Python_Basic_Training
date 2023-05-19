print('Задача 1. Имена')

# В базе данных одной компании есть баг (или, может быть, фича): если ввести туда имя сотрудника
# меньше чем из трёх букв, то база сломается и упадёт. Как компания принимает на работу людей,
# например, с китайскими именами, непонятно.
#
# Дан файл people.txt, в котором построчно хранится N имён пользователей.
#
# Напишите программу, которая берёт количество символов в каждой строке файла и в качестве ответа
# выводит общую сумму. Если в какой-либо строке меньше трёх символов (не считая литерала \n), то
# вызывается ошибка, и программа завершается.


sym_sum = 0
# line_count = 0
try:
    people_file = open('people.txt', 'r', encoding='utf-8')
    for i_line in people_file:
        length = len(i_line)
#        line_count += 1
        if i_line.endswith('\n'):
            length -= 1
        if 0 < length < 3:
            raise ValueError
            break
        sym_sum += length
    people_file.close()

except FileNotFoundError:
    print('Файл с именами не найден.')
except ValueError:
    print('Слишком короткое имя сотрудника.')
    sym_sum = 0
    raise BaseException
finally:
    print('Количество найденных символов:', sym_sum)
