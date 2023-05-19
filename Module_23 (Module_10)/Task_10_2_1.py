print('Задача 1. Пятый элемент.')

BRUCE_WILLIS = 42
input_data = input('Введите строку: ')
try:
    leeloo = int(input_data[4])
    result = BRUCE_WILLIS * leeloo
    print(f'- Leeloo Dallas! Multi-pass № {result}!')
except ValueError:
    print('Не удалось преобразовать 4 элемент в число.')
except IndexError:
    print('Нет данных для преобразования.')
except RuntimeError:
    print('Сегодня не ваш день...')
