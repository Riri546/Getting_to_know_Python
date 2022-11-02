from datetime import datetime as dt

def surname_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log_guide.csv', 'a') as file:
        file.write(f'surname: {data}\n')

def name_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log_guide.csv', 'a') as file:
        file.write(f'name: {data}\n')

def telephon_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log_guide.csv', 'a') as file:
        file.write(f'telephon: {data}\n')

def description_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log_guide.csv', 'a') as file:
        file.write(f'description: {data}\n')
