print('Задача 2. Сервер')

# У вас есть данные о сервере, которые хранятся в виде вот такого словаря:

server_data = {
    "server": {
        "host": "127.0.0.1",
        "port": "10"
    },
    "configuration": {
        "access": "true",
        "login": "Ivan",
        "password": "qwerty"
    }
}

# Напишите программу, которая выводит для пользователя эти данные так же
# красиво и понятно, как они представлены в словаре.

for i_item, i_details in server_data.items():
    print('\n', i_item, ':')
    for i_name, i_value in i_details.items():
        print('\t', i_name, ':', i_value)