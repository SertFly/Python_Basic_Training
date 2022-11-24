print('Задача 3. Контакты')


# Энтузиаст Степан, купив новый телефон, решил написать для него
# свою собственную операционную систему. И, конечно же, первое,
# что он захотел в ней реализовать, — это телефонная книга.

# Напишите программу, которая запрашивает у пользователя имя
# контакта и номер телефона, добавляет их в словарь и выводит
# на экран текущий словарь контактов. Запрос на добавление
# идёт бесконечно (но можно задать своё условие для завершения
# программы). Обеспечьте контроль ввода: если это имя уже есть
# в словаре, то выведите соответствующее сообщение.

def new_contact():
    name = input('\nВведите имя: ')
    if name in phone_book:
        print('Такой контакт уже существует...')
    else:
        phone_book[name] = input('Введите номер: ')
    return phone_book


phone_book = {}
while True:
    print('\nТекущие контакты на телефоне:')
    if phone_book:
        for i_name in phone_book:
            print(i_name, phone_book[i_name])
    else:
        print('<Пусто>')
    new_contact()