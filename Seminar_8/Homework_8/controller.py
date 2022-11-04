import sqlite3
import model as mod
import data_provider as data_prov


def button_click():
    while True:
        user_choice = input(
            '1 - просмотреть базу\n2 - добавить запись\n3 - удалить запись\n4 - найти по ФИО\nq - выход\n')
        if user_choice == '1':
            mod.previev_base()
        elif user_choice == '2':
            mod.add_record()
        elif user_choice == '3':
            id = input('Введите идентификационный номер сотрудника: ')
            mod.delete_record(id)
        elif user_choice == '4':
            mod.find_record()
        elif user_choice == 'q':
            print('Выход')
            break
        else:
            print('Не верно выбран режим работы')
