import sqlite3
import data_provider as data_prov

def previev_base():
    for i in data_prov.cursor.execute('SELECT * FROM personal'):
        print(*i)


def add_record():
    pass


def delete_record(id):
    data_prov.cursor.execute(f'DELETE from personal WHERE id={id}')
    data_prov.bd.commit()


def find_record(column, nam):
    data_prov.cursor.execute(f'select * from personal WHERE {column} LIKE "{nam}";')
    one = data_prov.cursor.fetchmany()
    return one


for i in data_prov.cursor.execute('SELECT * FROM personal'):
    print(*i)