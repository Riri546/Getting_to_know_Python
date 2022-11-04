def input_choice():
    while True:
        user_choice = input(
            '1 - просмотретьь базу, 2 - добавить запись, 3 - удалить запись, 4 найти по ФИО, q - выход')
        if user_choice == '1':
            previev_base()
        elif user_choice == '2':
            add_record()
        elif user_choice == '3':
            delete_record()
        elif user_choice == '4':
            find_record()
        elif user_choice == 'q':
            print('Выход')
            break
        else:
            print('Не верно выбран режим работы')
