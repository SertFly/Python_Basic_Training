print('Задача 2. Кризис фруктов')

# Мы работаем в одной небольшой торговой компании, где все данные о продажах
# фруктов за год сохранены в словаре в виде пар «название фрукта — доход»:

incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'grapefruit': 300.40,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
}
# В компании наступил небольшой кризис, и нам поручено провести небольшой
# анализ дохода.

# Напишите программу, которая находит общий доход, затем выводит фрукт с
# минимальным доходом и удаляет его из словаря. Выведите итоговый словарь
# на экран.

print('Общий доход:', sum(incomes.values()))
min_fruit = ''
for fruit in incomes:
    if incomes[fruit] == min(incomes.values()):
        min_fruit = fruit
        print(f'Минимальный доход у {fruit} {incomes.get(fruit)}')
incomes.pop(min_fruit)

print('Итоговый словарь:', incomes)
