print('Задача 2. Долги')

# Один наш друг занял у нас определённую сумму денег и всё никак не может их вернуть.
# А деньги нам нужны. Поэтому мы решили написать небольшой скрипт-напоминалку, который,
# возможно, разбудит его совесть.

# Напишите программу, которая получает на вход имя и долг, а затем выводит на экран
# сообщение, где имя повторяется несколько раз (и долг, возможно, тоже). Используйте
# числа в названиях ключей.

friend_name = input('Введите имя должника: ')
credit_amount = int(input('Сумма долга: '))

print(f'Привет, {friend_name}! Как твои дела, {friend_name}? Как поживают мои {credit_amount} рублей? '
      f'Когда ты, {friend_name}, вернешь мне мои любимые {credit_amount} рублей?' )