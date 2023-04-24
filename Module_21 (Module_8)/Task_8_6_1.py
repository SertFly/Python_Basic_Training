print('Задача 1. Работа с файлом')

# Вы пишете небольшое приложение для работы с файлами. Реализуйте функцию,
# которая может принимать на вход три аргумента: вопрос пользователю (на
# который нужно ответить да или нет), сообщение о неправильном вводе и
# количество попыток. Вопрос — обязательный позиционный аргумент, остальные —
# со значениями по умолчанию. При корректном ответе функция может возвращать
# что угодно — например, число 1 при ответе «да» или 0 при ответе «нет».

# В основной программе вызовите функцию минимум три раза: только с вопросом,
# с вопросом и сообщением об ошибке, с вопросом и количеством попыток.


def file_close_quiz(question, complaint='Неверный ввод. Пожалуйста, введите да или нет. ', retries=4):
    while True:
        answer = input(question).lower()
        if answer == 'да':
            return 1
        if answer == 'нет':
            return 0
        retries -= 1
        if retries == 0:
            print('Количество попыток истекло.')
            break
        print(complaint)
        print('Осталось попыток:', retries)

file_close_quiz('Вы действительно хотите выйти? ')
file_close_quiz('Удалить файл? ', 'Так удалить или нет? ')
file_close_quiz('Записать файл? ', retries=1)