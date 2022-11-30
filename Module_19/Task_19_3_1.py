print('Задача 1. Член семьи')

# Дана структура, которая содержит описание одного из членов семьи
# (имя, фамилия, хобби, сколько лет и дети):

family_member = {
    'name': 'Jane',
    'surname': 'Doe',
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "name": "Alice",
            "age": 6
        },
        {
            "name": "Bob",
            "age": 8
        }
    ]
}

# Напишите программу, которая реализует такую структуру: имя, фамилия,
# хобби, кол-во лет и дети. Затем, с помощью метода get и установки
# значения по умолчанию, проверьте есть ли ребёнок с именем Bob. Затем
# в отдельную переменную получите фамилию этого ребёнка и выведите её
# на экран. Если у него нет фамилии, то получите значение ‘Nosurname’.

children_dict = {}
for child in family_member["children"]:
    children_dict[child["name"]] = child["age"]

search_bob = children_dict.get("Bob", None)
if search_bob:
    print("Bob найден")
else:
    print("Bob-а нету!")

children_surname = family_member.get("surname", None)
if children_surname:
    print(children_surname)
else:
    print("No surname")
