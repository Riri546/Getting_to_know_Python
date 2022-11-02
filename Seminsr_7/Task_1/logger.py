from datetime import datetime as dt

def operation_logger(op, result):
    time = dt.now().strftime('%D - %H:%M')
    with open('log_complex.csv', 'a') as file:
        file.write(f'{op} = {result}\n')