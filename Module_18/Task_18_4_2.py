print('Задача 2. Путь к файлу')

# Все данные сайта лежат в одном проекте. При написании кода, внутри этого проекта
# часто используются абсолютные пути файлов, которые необходимо проверять.

# Пользователь вводит абсолютный путь к текстовому файлу, а также проверяемые данные:
# диск и расширение файла. Напишите программу, которая проверяет корректность этого пути.
userDisk = input('Выберите диск: ')
fileExtension = input('Введите расширение файла: ')
file_path = input('Введите абсолютный путь к файлу: ')
if file_path.startswith(userDisk) and file_path.endswith(fileExtension):
    print('Путь к файлу правильный')
else:
    print('Путь к файлу неверный')