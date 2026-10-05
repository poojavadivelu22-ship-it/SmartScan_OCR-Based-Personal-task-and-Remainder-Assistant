import sqlite3


DATABASE_NAME = "tasks.db"


# -------------------------------
# CREATE DATABASE
# -------------------------------

def create_database():

    connection = sqlite3.connect(
        DATABASE_NAME,
        check_same_thread=False
    )

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            task_date TEXT NOT NULL,
            task_time TEXT NOT NULL,
            status TEXT DEFAULT 'Pending'
        )
    """)

    connection.commit()
    connection.close()


# Create database automatically
create_database()


# -------------------------------
# ADD TASK
# -------------------------------

def add_task(task, task_date, task_time):

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO tasks
        (task, task_date, task_time, status)
        VALUES (?, ?, ?, ?)
    """, (
        task,
        task_date,
        task_time,
        "Pending"
    ))

    connection.commit()
    connection.close()


# -------------------------------
# GET TASKS
# -------------------------------

def get_tasks():

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, task, task_date, task_time, status
        FROM tasks
        ORDER BY task_date, task_time
    """)

    tasks = cursor.fetchall()

    connection.close()

    return tasks


# -------------------------------
# UPDATE TASK STATUS
# -------------------------------

def update_task_status(task_id):

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        UPDATE tasks
        SET status = 'Completed'
        WHERE id = ?
    """, (task_id,))

    connection.commit()
    connection.close()


# -------------------------------
# DELETE TASK
# -------------------------------

def delete_task(task_id):

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM tasks
        WHERE id = ?
    """, (task_id,))

    connection.commit()
    connection.close()