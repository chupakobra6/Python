letter = input('Введите любую букву латинского алфавита - ')    # Запрос у пользователя буквы латинского алфавита

if (letter == 'a') or (letter == 'e') or (letter == 'i') or (letter == 'o') or (letter == 'u'):    # Если введенная буква входит в следующий список (a, e, i, o или u)
    print('Введённая буква - гласная')    # необходимо вывести сообщение о том, что эта буква гласная
elif letter == 'y':    # Если была введена буква y
    print('Введённая буква может быть и гласной, и согласной')    # программа должна написать что эта буква может быть как гласной, так и согласной
else:    # Во всех других случаях
    print('Введённая буква - согласная')    # должно выводиться сообщение о том, что введена согласная буква

quit = input('Нажмите Enter для выхода из программы') # прописываем input для ожидания выхода из программы