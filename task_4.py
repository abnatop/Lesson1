# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции

counter = 0
digit = input('Введите целое положительное число: ')
max_digit = digit[0]

while counter < len(digit):
    if digit[counter] > max_digit:
        max_digit = digit[counter]
    counter += 1

print(max_digit)