# 8.Определить, является ли год, который ввел пользователь, високосным или не високосным.

year = int(input('Введите год:'))

if year % 4 != 0:
    print('Год обычный')
else:
    print('Год високосный')