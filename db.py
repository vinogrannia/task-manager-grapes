import sqlite3

def get_connection():
    connection = sqlite3.connect("tasks.db")
    connection.row_factory = sqlite3.Row
    return connection

def initialize_db():
    connection = get_connection()
    connection.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        completed INTEGER NOT NULL CHECK (completed IN (0, 1)) DEFAULT 0
    )
    ''')
    connection.commit()
    connection.close()

def add_task(title):
    connection = get_connection()
    connection.execute('INSERT INTO tasks (title, completed) VALUES (?, ?)', (title, 0))
    connection.commit()
    connection.close()

def get_tasks():
    connection = get_connection()
    cursor = connection.execute("SELECT id, title, completed FROM tasks ORDER BY id DESC")
    rows = cursor.fetchall()
    connection.close()
    return rows

def get_task(task_id):
    connection = get_connection()
    cursor = connection.execute("SELECT id, title, completed FROM tasks WHERE id = ?", (task_id,))
    row = cursor.fetchone()
    connection.close()
    return row

def edit_task(task_id, title):
    connection = get_connection()
    connection.execute('UPDATE tasks SET title = ? WHERE id = ?', (title, task_id))
    connection.commit()
    connection.close()

def complete_task(task_id):
    connection = get_connection()
    connection.execute('UPDATE tasks SET completed = 1 WHERE id = ?', (task_id,))
    connection.commit()
    connection.close()

def delete_task(task_id):
    connection = get_connection()
    connection.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    connection.commit()
    connection.close()

