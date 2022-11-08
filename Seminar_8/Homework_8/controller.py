import sqlite3
import model as mod


def button_click():
    while True:
        user_choice = input(
            '1 - просмотреть базу\n2 - добавить запись\n3 - удалить запись\n4 - изменение размера оклада\n5 - измение размера премии\nq - выход\n')
        if user_choice == '1':
            mod.previev_base()
        elif user_choice == '2':
            mod.add_record()
        elif user_choice == '3':
            id = input('Введите идентификационный номер сотрудника: ')
            mod.delete_record(id)
        elif user_choice == '4':
            id = input('Введите идентификационный номер сотрудника: ')
            salary = input('Введите новую сумму оклада сотрудника: ')
            mod.salary_record(id, salary)
        elif user_choice == '5':
            id = input('Введите идентификационный номер сотрудника: ')
            bonus = input('Введите новую сумму премии сотрудника: ')
            mod.bonus_record(id, bonus)
        elif user_choice == 'q':
            print('Выход')
            break
        else:
            print('Не верно выбран режим работы')
