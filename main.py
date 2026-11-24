
from task_operation import add_task, view_tasks
from task_crud import (
    update_task,
    delete_task,
    complete_task,
    search_task, sort_task, filter_task
)
from database import create_table, add_due_date_column


# Initialize SQLite database
create_table()
add_due_date_column()

while True:
    print("\n===== PYTHON TASK MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Completed")
    print("6. Search Task")
    print("7. Filter Tasks")
    print("8. Sort Tasks")
    print("9. Exit")

    try:
        choice = int(input("Enter your choice: "))

    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    if choice == 1:
        add_task()

    elif choice == 2:
        view_tasks()

    elif choice == 3:
        update_task()

    elif choice == 4:
        delete_task()

    elif choice == 5:
        complete_task()

    elif choice == 6:
        search_task()

    elif choice == 7:
       filter_task()
    
    elif choice == 8:
       sort_task()    

    elif choice == 9:
        print("Exiting Task Manager...")
        break

    else:
        print("Invalid choice!")
