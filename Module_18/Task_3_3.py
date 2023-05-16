print('Задача 3. Разделители символов')

# Человек хочет сделать рассылку поздравлений для определённого списка людей.
# Поздравления для разных людей он хочет написать по-разному.

# Напишите программу, которая запрашивает у пользователя:
# Шаблон поздравления (туда вставляется ФИ и возраст)
# ФИ людей (в одну строку, разделяются запятой)
# Возраст каждого человека (в одну строку через пробел)

# В конце программа выводит поздравления и всех именинников в одну строку
# вместе с их возрастом.

while True:
    congrats_template = input('Введите текст поздравления с использованием конструкций '
                              '{name} и {age}: '
                              )
    if '{name}' in congrats_template and '{age}' in congrats_template:
        break
    print('Неправильный шаблон поздравления: отсутствует одна или две конструкции.')

while True:
    names_list = input('Введите имена через запятую: ').split(', ')
    ages_list = input('Введите возраст каждого через пробел: ').split()
    ages = [int(i_num) for i_num in ages_list]
    if len(names_list) == len(ages):
        break
    print('Проверьте данные, список имен не соответствует списку возрастов.')

for i_man in range(len(names_list)):
    print(congrats_template.format(name=names_list[i_man], age=ages[i_man]))

print([' - '.join([names_list[i], str(ages_list[i])]) for i in range(len(names_list))])
