import sqlite3

bd = sqlite3.connect("Data_base.db")

cursor = bd.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS personal(
    id INT,
    name TEXT,
    last_name TEXT,
    position TEXT,
    salary INT,
    bonus INT
)''')

baza = [(1, 'Иван', 'Иванов', 'главный инженер', 500000, 10000),
(2, 'Вадим', 'Корпатый', 'инженер', 551100, 2300),
(3, 'Грегорий', 'Саломохин', 'бухгалтер', 230000, 100)]

cursor.executemany('INSERT INTO personal VALUES(?,?,?,?,?,?)',baza)
bd.commit()

for i in cursor.execute('SELECT * FROM personal'):
    print(*i)

cursor.execute('DELETE from personal WHERE')

for i in cursor.execute('SELECT * FROM personal'):
    print(*i)

cursor.execute('DELETE from personal WRETE id=1')