print('Задача 3. Поиск элемента')

# Когда мы работаем с большой многоуровневой структурой, нам нередко необходимо
# пройтись по ней и найти нужный элемент. Для этого в программировании используются
# специальные алгоритмы поиска.

# Напишите функцию, которая находит заданный пользователем ключ в словаре и выдаёт
# значение этого ключа на экран. В качестве примера можно использовать такой словарь:

site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def key_search(key, site):
    if key in site:
        return site[key]

    for i_site in site.values():
        if isinstance(i_site, dict):
            result = key_search(key, i_site)
            if result:
                break
    else:
        result = None
    return result


key = input('Какой ключ Вы хотите найти? ')
if key_search(key, site) is None:
    print('Ключ не найден.')
else:
    print('Значение ключа: ', key_search(key, site))