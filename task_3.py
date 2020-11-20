# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

digit = input('Введите целое число: ')

digit_one = int(digit)
digit_two = int(digit * 2)
digit_three = int(digit * 3)
result = digit_one + digit_two + digit_three

print(result)