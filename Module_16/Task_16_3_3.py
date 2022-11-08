print('Задача 3. Пакеты')

# При работе с сервером мы кодируем сообщение и отправляем его в виде пакетов информации.
# Их количество равно N. Допустим, каждый пакет содержит четыре числа, каждое из которых
# равно нулю или единице. Эти числа называются битами. Иногда в кодировке сообщения
# встречаются ошибки, и в пакете эта ошибка обозначается числом -1. Если таких ошибок не
# больше одной, то этот пакет мы целиком добавляем в список для декодирования, а иначе
# отбрасываем.

# Напишите программу, которая будет обрабатывать полученные пакеты и выведет на экран
# итоговое сообщение для декодирования, а также количество ошибок в нём и количество
# необработанных пакетов.

number = int(input('\nВведите количество пакетов для обработки: '))
common_package = []
bad_package_counter = 0

for i in range(number):
    temp_package = []
    print(f'\nВведите {i + 1} пакет:')
    for bit in range(4):
        temp_package.append(int(input(f'Введите значение {bit + 1} бита: ')))
    if temp_package.count(-1) < 2:
        common_package.extend(temp_package)
    else:
        bad_package_counter += 1

print('\nИтоговое сообщение для декодирования:', common_package)
print('Кол-во ошибок в сообщении', common_package.count(-1))
print('Кол-во необработанных пакетов:', bad_package_counter)