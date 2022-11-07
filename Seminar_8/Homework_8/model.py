import sqlite3
import data_provider as data_prov
import controller as c


def previev_base():
    for i in data_prov.cursor.execute('SELECT * FROM personal'):
        print(*i)


def add_record():
    new_baza = [(5, 'Марк', 'Иванченко', 27, 'механник', 300000, 15000),
        (6, 'Дмитрий', 'Дюдин', 34, 'оператор ЧПУ', 54400, 6500),
        (7, 'Елизавета', 'Сильвер', 21, 'стажер', 20000, 1000)]
    try:
        data_prov.cursor.executemany('INSERT INTO personal VALUES(?,?,?,?,?,?,?)', new_baza)
        data_prov.bd.commit()
    except:
        print('Данные уже есть\n')


def delete_record(id):
    data_prov.cursor.execute(f'DELETE from personal WHERE id={id}')
    print(f'Удален сотрудник с идентификационным номером {id}')
    data_prov.bd.commit()

def salary_record(id, salary):
    data_prov.cursor.execute(f'UPDATE personal SET salary={salary} WHERE id={id};')
    data_prov.bd.commit()
    print(f'Оклад изсенен на сумму {salary}')

def bonus_record(id, bonus):
    data_prov.cursor.execute(f'UPDATE personal SET bonus={bonus} WHERE id={id};')
    data_prov.bd.commit()
    print(f'Размер премии изсенен на сумму {bonus}')



