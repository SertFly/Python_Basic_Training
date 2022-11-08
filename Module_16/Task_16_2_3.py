print('Задача 3. Кино')

# Мы поддерживаем свой киносайт и хотим сделать так, чтобы пользователи после регистрации могли
# создать собственный рейтинг фильмов из тех, которые есть на сайте. Вот сам список фильмов
# (конечно же, можете брать свои):

films = [
    'Крепкий орешек', 'Назад в будущее', 'Леон', 'Богемская рапсодия',
    'Проклятый остров', 'Начало', 'Матрица', 'Джентльмены', 'Однажды в Ирландии',
    'Тор', 'Тор 2', 'Капитан Америка', 'Ворошиловский стрелок', 'Брат', 'Ночь в музее'
]
favorite_films = []

# Напишите программу, которая позволяет добавлять в свой рейтинг фильмы, удалять их оттуда,
# а также вставлять на нужное пользователю место. Обеспечьте контроль ввода и сделайте так,
# чтобы в список нельзя было добавить один и тот же фильм несколько раз.

def action_add(favorite_films, film_name):
    if film_name not in favorite_films:
        favorite_films.append(film_name)
    else:
        print('Фильм уже добавлен в рейтинг!')


def action_insert(favorite_films, film_name):
    if film_name not in favorite_films:
        i_film = int(input('На какое место поставим этот фильм? '))
        favorite_films.insert(i_film - 1, film_name)
    else:
        print('Фильм уже добавлен в рейтинг!')


def action_remove(favorite_films, film_name):
    if film_name not in favorite_films:
        print('Этого фильма нет в вашем рейтинге!')
    else:
        favorite_films.remove(film_name)


while True:
    print('\nВаш текущий рейтинг фильмов:', favorite_films)
    film_name = input('Название фильма: ')
    if film_name not in films:
        print('Фильма нет на сайте...')
    else:
        print('\nКоманды: добавить, вставить, удалить.')
        action = input('Введите команду: ')
        if action == 'Добавить' or action == 'добавить':
            action_add(favorite_films, film_name)
        elif action == 'Вставить' or action == 'вставить':
            action_insert(favorite_films, film_name)
        elif action == 'Удалить' or action == 'удалить':
            action_remove(favorite_films, film_name)
        else:
            print('Неправильная команда, повторите ввод.')

