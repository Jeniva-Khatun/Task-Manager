
import sqlite3
import json
import os

#Connect to the database
def create_connection():
    connection = sqlite3.connect("data/tasks.db")
    return connection


#Create the tasks table
def create_table():
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            priority TEXT,
            status TEXT
        )
    """)

    connection.commit()
    connection.close()




#insert a new task
def insert_task(title, description,priority,status,due_date):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO tasks(title,description,priority,status,due_date)
        VALUES(?,?,?,?,?)
    
    """,(title,description,priority,status,due_date))

    connection.commit()
    connection.close()






#retrieve all task

def get_all_tasks():
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    connection.close()
    return tasks

def search_tasks_by_title(keyword):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM tasks
        WHERE title LIKE ?
    """, ('%' + keyword + '%',))

    tasks = cursor.fetchall()
    connection.close()

    return tasks


def filter_tasks(status=None, priority=None):
    connection = create_connection()
    cursor = connection.cursor()

    query = "SELECT * FROM tasks WHERE 1=1"
    values = []

    if status:
        query += " AND status = ?"
        values.append(status)

    if priority:
        query += " AND priority = ?"
        values.append(priority)

    cursor.execute(query, values)

    tasks = cursor.fetchall()
    connection.close()

    return tasks


def get_sorted_tasks(sort_by):
    connection = create_connection()
    cursor = connection.cursor()

    if sort_by == "due_date":
        cursor.execute("""
            SELECT * FROM tasks
            ORDER BY
                CASE
                    WHEN due_date IS NULL OR due_date = '' THEN 1
                    ELSE 0
                END,
                due_date ASC
        """)

    elif sort_by == "priority":
        cursor.execute("""
            SELECT * FROM tasks
            ORDER BY
                CASE LOWER(priority)
                    WHEN 'high' THEN 1
                    WHEN 'medium' THEN 2
                    WHEN 'low' THEN 3
                    ELSE 4
                END
        """)

    tasks = cursor.fetchall()
    connection.close()

    return tasks



def delete_tasks(task_id):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute(
         "DELETE FROM tasks WHERE id = ? ",
         (task_id,)
         )

    connection.commit()
    if cursor.rowcount > 0:
        print("Task deleted successfully!")
    else:
        print("Task ID not found!")

    connection.close()

def update_task(task_id, new_title):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute (
         "UPDATE tasks SET title = ? WHERE id = ?",
         (new_title, task_id)

    )
    connection.commit()

    if cursor.rowcount > 0:
         print("Task updated successfully!")
    else:
        print("Task ID not found!")

    connection.close() 

def complete_task(task_id):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute(
        "UPDATE tasks SET status = ? WHERE id = ?",
        ("Completed", task_id)
    )

    connection.commit()

    if cursor.rowcount > 0:
        print("Task marked as completed!")
    else:
        print("Task ID not found!")

    connection.close()

# Add due_date column to the existing tasks table

def add_due_date_column():
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("PRAGMA table_info(tasks)")
    columns = cursor.fetchall()

    column_names = [column[1] for column in columns]

    if "due_date" not in column_names:
        cursor.execute("""
            ALTER TABLE tasks
            ADD COLUMN due_date TEXT
        """)

        connection.commit()
        print("Due date column added successfully!")

    connection.close()

def reset_database():
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM tasks")
    cursor.execute(
        "DELETE FROM sqlite_sequence WHERE name = 'tasks'"
    )

    connection.commit()
    connection.close()

    print("Database reset successfully!")    

     
        

#Run this code only when database.py is executed directly


if __name__ == "__main__":
    create_table()
    print("Database initialized successfully!")

    add_due_date_column()

    print("\n===== ALL TASKS =====")

    tasks = get_all_tasks()

    if tasks:
        for task in tasks:
            print(task)
    else:
        print("No task found!")
        
