a = int(input('Введите целое число - '))  # Дано целое число

if a > 0:  # Если оно является положительным, то прибавить нему 1
    a += 1
elif a < 0:  # Eсли отрицательным, то вычесть из него 2
    a -= 2
else:  # Eсли нулевым, то заменить его на 10
    a = 10

print('Изменённое число = ', a)  # Вывести полученно число

quit = input('Нажмите Enter для выхода из программы') # прописываем input для ожидания выхода из программы
