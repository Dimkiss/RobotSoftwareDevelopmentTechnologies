import sqlite3
from faker import Faker
import random

conn = sqlite3.connect('company_data.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Projects (
    project_id INTEGER PRIMARY KEY,
    project_name TEXT,
    manager TEXT,
    budget REAL,
    spent REAL,
    deadline TEXT
)
''')

cursor.execute("DELETE FROM Projects")

fake = Faker()
for _ in range(100):
    project_name = fake.bs().capitalize()
    manager = fake.name()
    budget = random.uniform(50_000, 500_000)
    spent = random.uniform(0, budget)
    deadline = fake.date_between(start_date="+10d", end_date="+365d")
    cursor.execute(
        '''
        INSERT INTO Projects (project_name, manager, budget, spent, deadline)
        VALUES (?, ?, ?, ?, ?)
        ''',
        (project_name, manager, budget, spent, deadline)
    )

conn.commit()
conn.close()

print("таблица Projects создана и заполнена данными.")
