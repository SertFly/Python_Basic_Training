print('Задача 2. Олимпиада')
# В олимпиаде по программированию участвует N человек, в списке участников они обозначаются
# под номерами 1, 2, 3, 4 и так далее до N. Эти участники поделены на команды по K человек.

# Напишите программу, которая принимает на вход количество участников и количество человек
# в каждой команде, затем генерирует список таких команд и выводит его на экран.

# Обеспечьте контроль ввода: в каждой команде должно быть ровно по K человек.

members = int(input('Сколько человек участвует в олимпиаде: '))
teams = int(input('На сколько команд разделены все участники: '))
members_arrange = []
num = 1
if members % teams != 0:
    print('Не удалось разделить всех участников на равные команды!')
else:
    for i_team in range(teams):
        members_arrange.append(list(range(num, num + members//teams)))
        num += members//teams

    print('Общая раскладка участников по командам:', members_arrange )

