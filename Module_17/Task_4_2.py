print('Задача 2. Срезы')

# Дан список чисел:
nums = [48, -10, 9, 38, 17, 50, -5, 43, 46, 12]

# Напишите программу, которая выводит на экран шесть ответов:
#
# В первой строке выведите первые пять элементов списка.
# Во второй строке выведите весь список, кроме последних двух элементов.
# В третьей строке выведите все элементы с чётными индексами.
# В четвёртой строке выведите все элементы с нечётными индексами.
# В пятой строке выведите все элементы в обратном порядке.
# В шестой строке выведите все элементы списка через один в обратном порядке, начиная с последнего.

# Для решения используйте только срезы (и без функции len).

print('\nРезультаты: ')
print('1)', nums[0:5])
print('2)', nums[0:8])
print('3)', nums[0:10:2])
print('4)', nums[1:10:2])
print('5)', nums[::-1])
print('6)', nums[::-2])
