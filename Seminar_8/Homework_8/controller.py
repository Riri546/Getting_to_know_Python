import sqlite3
import model as mod


def input_choice():
    while True:
        user_choice = input(
            '1 - просмотретьь базу, 2 - добавить запись, 3 - удалить запись, 4 найти по ФИО, q - выход')
        if user_choice == '1':
            mod.previev_base()
        elif user_choice == '2':
            mod.add_record()
        elif user_choice == '3':
            mod.delete_record()
        elif user_choice == '4':
            mod.find_record()
        elif user_choice == 'q':
            print('Выход')
            break
        else:
            print('Не верно выбран режим работы')
