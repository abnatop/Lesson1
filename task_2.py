# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

time_seconds = int(input('Введите время в секундах: '))

minutes, seconds = divmod(time_seconds, 60)
hours, minutes = divmod(minutes, 60)
print("%02d:%02d:%02d" % (hours, minutes, seconds))

# либо так
# import time
# print(time.strftime("%H:%M:%S", time.gmtime(time_seconds)))