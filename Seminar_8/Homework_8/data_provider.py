import sqlite3


bd = sqlite3.connect("Data_base.db")
cursor = bd.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS personal(
    id INTEGER PRIMARY KEY autoincrement,
    name TEXT,
    last_name TEXT,
    age INT,
    position TEXT,
    salary INT,
    bonus INT
)''')


baza = [(1, 'Иван', 'Иванов', 35, 'главный инженер', 500000, 10000),
        (2, 'Вадим', 'Корпатый', 25, 'инженер', 551100, 2300),
        (3, 'Грегорий', 'Саломохин', 40, 'бухгалтер', 230000, 100)]

try:
    cursor.executemany('INSERT INTO personal VALUES(?,?,?,?,?,?,?)', baza)
    bd.commit()
except:
    print('Данные уже есть\n')
