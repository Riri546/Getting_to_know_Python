import sqlite3
import data_provider as data_prov


def previev_base():
    for i in data_prov.cursor.execute('SELECT * FROM personal'):
        print(*i)


# def add_record(id, name, last_name, age, position, salary, bonus):
#     data_prov.cursor.execute("SELECT * FROM personal")
#     data_prov.cursor.executemany('INSERT INTO personal VALUES(?,?,?,?,?,?)',id, name, last_name, age, position, salary, bonus)   
#     data_prov.bd.commit()


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
