import sqlite3

connecction = sqlite3.connect("tasks")
cursor = connecction.cursor()
cursor.execute(
    "CREATE TABLE IF NOT EXISTS task (" \
    "   title TEXT, " \
    "   description TEXT" \
    ")" \
)

# Gets a table and prints it row by row (Debug only)
def log_tasks():
    rows = cursor.execute("SELECT * FROM task").fetchall()
    if len(rows) == 0:
        print("There are no tasks stored in the database")
    else:  
        for row in rows:
            print(row)

def list_tasks(title_filter: str | None, description_filter: str | None):
    # Gets the tasks from the database
    tasks = cursor.execute("SELECT * FROM task").fetchall()
    if len(tasks) == 0:
        print("You haven't created any tasks yet")
    else:
        for task in tasks:
            # Checks if the task is valid according to the filters provided
            is_task_valid: bool = False
            if title_filter != None:
                words = task[0].split()
                for word in words:
                    if word == title_filter:
                        is_task_valid = True
            if description_filter != None:
                if task[1] == None:
                    continue
                words = task[1].split()
                for word in words:
                    if word == description_filter:
                        is_task_valid = True
            if title_filter == None and description_filter == None:
                is_task_valid = True
            if is_task_valid:
                '''
                0: Task title
                1: Task description
                '''
                print("[] - " + task[0])
                if task[1] != None:
                    print("    " + task[1])
    

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
