print('Задача 3. Собачьи бега')

# В собачьих бегах участвует N собак, у каждой из них есть определённое количество очков за сезон.
# На огромном табло выводятся очки каждой собаки. Однако при выводе был обнаружен баг:
# собаки с наибольшим и наименьшим количеством очков поменялись местами! Нужно это исправить.
# Дан список очков из N собак. Напишите программу, которая меняет местами наибольший и наименьший элементы в списке.

numbers = int(input('Введите количество собак в сезоне: '))
scores = []
print()

for i in range(numbers):
    score = int(input(f'Введите очки {i + 1} собаки: '))
    scores.append(score)

maximum = scores[0]
minimum = scores[0]
i = 0
max_i = min_i = 0

for num in scores:
    if maximum < num:
        maximum = num
        max_i = i
    if minimum > num:
        minimum = num
        min_i = i
    i += 1

scores[max_i] = minimum
scores[min_i] = maximum
i = 0
print()

for score in scores:
    print(f'Очки собаки {i + 1} равны {score}')
    i += 1
