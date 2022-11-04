def previev_base():
    for i in cursor.execute('SELECT * FROM personal'):
        print(*i)


def add_record():
    pass


def delete_record(id):
    cursor.execute(f'DELETE from personal WHERE id={id}')
    bd.commit()


def find_record(column, nam):
    cursor.execute(f'select * from personal WHERE {column} LIKE "{nam}";')
    one = cursor.fetchmany()
    return one


for i in cursor.execute('SELECT * FROM personal'):
    print(*i)