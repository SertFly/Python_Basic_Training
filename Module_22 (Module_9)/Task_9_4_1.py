print('Задача 1. Сумма чисел')

# Во входном файле numbers.txt записано N целых чисел, каждое в отдельной строке.
# Напишите программу, которая выводит их сумму в выходной файл answer.txt.

numbers_file = open('numbers.txt', 'r')
summa = 0
for i_line in numbers_file:
    summa += int(i_line)
numbers_file.close()
answers = open('answers.txt', 'w')
answers.write(str(summa))
answers.close()

