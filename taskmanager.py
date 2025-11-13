import sqlite3

connecction = sqlite3.connect("tasks")
cursor = connecction.cursor()
cursor.execute(
    "CREATE TABLE IF NOT EXISTS task (" \
    "   title TEXT, " \
    "   description TEXT" \
    ")" \
)

# Gets a table and prints it row by row
def log_tasks():
    rows = cursor.execute("SELECT * FROM task").fetchall()
    if len(rows) == 0:
        print("There are no tasks stored in the database")
    else:  
        for row in rows:
            print(row)

# Adds a new task
def add_task(title: str, description: str):
    try:
        cursor.execute(
            "INSERT INTO task (title, description) VALUES (?, ?)",
            (title, description)
        )
        connecction.commit()
        print("The task was created successfully")
    except:
        print("The creation of the task failed. Please try again")
