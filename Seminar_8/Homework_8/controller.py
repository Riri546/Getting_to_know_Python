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
            id = input('\nВведите идентификационный номер сотрудника: ')
            name = input('\nВведите имя сотрудника: ')
            last_name = input('\nВведите фамилтию сотрудника: ')
            age = input('\nВведите возраст сотрудника: ')
            position = input('\nВведите должность сотрудника: ')
            salary = input('\nВведите размер заработной платы сотрудника: ')
            bonus = input('\nВведите размер премии: ')
            mod.add_record(id, name, last_name, age, position, salary, bonus)
        elif user_choice == '3':
            id = input('Введите идентификационный номер сотрудника: ')
            mod.delete_record(id)
        elif user_choice == '4':
            column = input('Введите название колонки:')
            nam = ('Введите данные для изменения')
            mod.find_record(column, nam)
        elif user_choice == 'q':
            print('Выход')
            break
        else:
            print('Не верно выбран режим работы')
