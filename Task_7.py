# 7.По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника, составленного из этих отрезков.
# Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или равносторонним.

print('Далее вам предложат ввести длины сторон треугольника')

a = int(input('Введите длину стороны a :'))
b = int(input('Введите длину стороны b :'))
c = int(input('Введите длину стороны c :'))

if a + b <= c or a + c <= b or b + c <= a:
    print('Треугольник не существует')
elif a != b and a != c and b != c:
    print('Треугольник разносторонний')
elif a == b == c:
    print('Треугольник равносторонний')
else:
    print('Треугольник равнобедренный')