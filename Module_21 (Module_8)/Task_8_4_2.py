print('Задача 2. Непонятно!')

# Друг никак не может понять эту тему с изменяемыми и неизменяемыми типами,
# ссылками, объектами и их id. Видя, как он мучается, вы решили помочь ему
# и объяснить эту тему наглядно.

# Пользователь вводит любой объект. Напишите программу, которая выводит на
# экран тип введённых данных, информацию о его изменяемости, а также id
# этого объекта.

data_names_dict = {
    "<class 'str'>": "строка",
    "<class 'dict'>": "словарь",
    "<class 'list'>": "список",
    "<class 'set'>": "множество"
}

mutable_check_helper = {
    "mutable": ("словарь", "список", "множество")
}


def check_info(data):
    type_of_data = type(data)
    name_of_data = ""
    if str(type_of_data) in data_names_dict:
        name_of_data = data_names_dict[str(type_of_data)]

    if name_of_data in mutable_check_helper["mutable"]:
        property_of_data = "Изменяемый (mutable)"
    else:
        property_of_data = "Неизменяемый (immutable)"

    print(f"Тип данных: {type_of_data} ({name_of_data})")
    print(property_of_data)
    print("Id объекта:", id(data))


data_in = 'привет'
check_info(data_in)
