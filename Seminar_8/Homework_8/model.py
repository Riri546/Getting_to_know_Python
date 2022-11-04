import sqlite3
import data_provider as data_prov


def previev_base():
    for i in data_prov.cursor.execute('SELECT * FROM personal'):
        print(*i)


# def add_record(id, name, last_name, age, position, salary, bonus):
    # id = input('Введите идентификационный номер сотрудника: \n')
    # name = input('Введите имя сотрудника: \n')
    # last_name = input('Введите фамилтию сотрудника: \n')
    # age = input('Введите возраст сотрудника: \n')
    # position = input('Введите должность сотрудника: \n')
    # salary = input('Введите размер заработной платы сотрудника: \n')
    # bonus = input('Введите размер премии: \n')
    # data_prov.cursor.executemany(f'INSERT INTO personal (id, name, last_name, age, position, salary, bonus)\
    # VALUES({id}, {name}, {last_name}, {age}, {position}, {salary}, {bonus})')
def add_record():
    data_prov.cursor.execute("""INSERT INTO personal
                            (id, name, last_name, age, position, salary, bonus)
                            VALUES
                            (1, 'Иван', 'Иванов', 35, 'главный инженер', 500000, 10000);""")
    data_prov.bd.commit()


def delete_record(id):
    data_prov.cursor.execute(f'DELETE from personal WHERE id={id}')
    print(f'Удален сотрудник с идентификационным номером {id}')
    data_prov.bd.commit()


def find_record(column, nam):
    data_prov.cursor.execute(
        f'select * from personal WHERE {column} LIKE "{nam}";')
    one = data_prov.cursor.fetchmany()
    return one


for i in data_prov.cursor.execute('SELECT * FROM personal'):
    print(*i)
