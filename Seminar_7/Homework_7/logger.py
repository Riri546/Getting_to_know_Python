def surname_logger(data):
    with open('log_telephon.csv', 'a') as file:
        file.write(f'Surname: {data}\n')


def name_logger(data):
    with open('log_telephon.csv', 'a') as file:
        file.write(f'Name: {data}\n')


def telephon_logger(data):
    with open('log_telephon.csv', 'a') as file:
        file.write(f'Telephon: {data}\n')


def description_logger(data):
    with open('log_telephon.csv', 'a') as file:
        file.write(f'Description: {data}\n''\n')
