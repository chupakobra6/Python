a = float(input('Введите вещественную переменную A - '))
b = float(input('Введите вещественную переменную B - '))    # Даны три переменные вещественного типа: A, B, C
c = float(input('Введите вещественную переменную C - '))

if a < b and b < c:    # Если их значения упорядочены по возрастанию, то удвоить их
    a *= 2
    b *= 2
    c *= 2
else:                  # в противном случае заменить значение каждой переменной на противоположное
    a *= -1
    b *= -1
    c *= -1

print(f'Новые значения переменных A = {a}, B = {b}, C = {c}')    # Вывести новые значения переменных A, B, C

quit = input('Нажмите Enter для выхода из программы') # прописываем input для ожидания выхода из программы
