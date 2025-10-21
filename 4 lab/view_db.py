import sqlite3
import pandas as pd

# посмотреть в терминале полностью
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)

conn = sqlite3.connect("company_data.db")

tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", conn)
print("таблицы в базе данных:")
print(tables)

def show_table(name):
    try:
        df = pd.read_sql_query(f"SELECT * FROM {name};", conn)
        print(f"\nданные из таблицы {name}:")
        print(df)  # показываем всю таблицу
    except Exception:
        print(f"\nтаблица {name} не найдена в базе данных.")

show_table("Projects")
show_table("project_finance_status")

conn.close()
