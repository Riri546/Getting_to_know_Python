def surname_logger(data):
    with open('log_guide.csv', 'a') as file:
        file.write(f'surname: {data}\n')


def name_logger(data):
    with open('log_guide.csv', 'a') as file:
        file.write(f'name: {data}\n')


def telephon_logger(data):
    with open('log_guide.csv', 'a') as file:
        file.write(f'telephon: {data}\n')


def description_logger(data):
    with open('log_guide.csv', 'a') as file:
        file.write(f'description: {data}\n''\n')
