import sqlite3

conn = sqlite3.connect('company_data.db')
cursor = conn.cursor()

cursor.execute("SELECT project_id, project_name, manager, budget, spent, deadline FROM Projects")
projects = cursor.fetchall()

cursor.execute('''
CREATE TABLE IF NOT EXISTS project_finance_status (
    project_id INTEGER,
    project_name TEXT,
    manager TEXT,
    budget REAL,
    spent REAL,
    deadline TEXT,
    utilization_percent REAL,
    status TEXT
)
''')

cursor.execute("DELETE FROM project_finance_status")

for project_id, name, manager, budget, spent, deadline in projects:
    utilization_percent = round((spent / budget) * 100, 2)
    status = "Рисковый" if utilization_percent > 90 else "Стабильный"
    cursor.execute(
        '''
        INSERT INTO project_finance_status 
        (project_id, project_name, manager, budget, spent, deadline, utilization_percent, status)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (project_id, name, manager, budget, spent, deadline, utilization_percent, status)
    )

conn.commit()
conn.close()
print("таблица project_finance_status создана и заполнена.")
