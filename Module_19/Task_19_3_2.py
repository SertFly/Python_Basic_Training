print('Задача 2. Игроки')

# Есть готовый словарь игроков, у каждого игрока есть имя, команда,
# в которой он играет, а также его текущий статус, в котором указано,
# отдыхает он, тренируется или путешествует:

players_dict = {
    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
}
status_dict = {
    'Rest': 'отдыхают',
    'Training': 'тренируются',
    'Travel': 'путешествуют'
}

teams_list = ['A', 'B', 'C']

# Напишите программу, которая выводит на экран вот такие данные в разных строчках:

# Все члены команды из группы B, которые тренируются.
# Все члены команды из команды C, которые путешествуют.
# Все члены команды из команды А, которые отдыхают.

for index, state in enumerate(status_dict):
    print(f"Все члены команды из команды {teams_list[index]}, которые {status_dict[state]}:")
    for _, player in players_dict.items():
        if player["status"] == state and player["team"] == teams_list[index]:
            print(player["name"])
