from datetime import datetime as dt

def surname_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log_guide.csv', 'a') as file:
        file.write(f'{time}: {data}\n')

def name_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log_guide.csv', 'a') as file:
        file.write(f'{time}: {data}\n')

def telephon_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log_guide.csv', 'a') as file:
        file.write(f'{time}: {data}\n')

def description_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log_guide.csv', 'a') as file:
        file.write(f'{time}: {data}\n')


# def temperature_logger(data):
#     time = dt.now().strftime('%H:%M')
#     with open('log_guide.csv', 'a') as file:
#         file.write('{}; temperature; {}\n'
#                    .format(time, data))


# def pressure_logger(data):
#     time = dt.now().strftime('%H:%M')
#     with open('log_guide.csv', 'a') as file:
#         file.write('{}; pressure; {}\n'
#                    .format(time, data))


# def wind_speed_logger(data):
#     time = dt.now().strftime('%H:%M')
#     with open('log_guide.csv', 'a') as file:
#         file.write('{}; wind speed; {}\n'
#                    .format(time, data))
