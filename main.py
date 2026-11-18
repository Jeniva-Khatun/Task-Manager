from task_operation import add_task, view_tasks
from task_crud import update_task, delete_task, complete_task, search_task
from task_storage import load_tasks , save_tasks

# Load saved tasks
tasks = load_tasks()

# Stop if saved data cannot be loaded safely
if tasks is None:
    print("Task Manager cannot start because the saved data is invalid.")
    raise SystemExit(1)

while True:
    print("===== PYTHON TASK MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Completed")
    print("6. Search Task")
    print("7. Exit")

    try:
        choice = int(input("Enter your choice: "))

    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    if choice == 1:
        add_task(tasks)
        save_tasks(tasks)

    elif choice == 2:
        view_tasks(tasks)

    elif choice == 3:
        update_task(tasks)
        save_tasks(tasks)

    elif choice == 4:
        delete_task(tasks)
        save_tasks(tasks)

    elif choice == 5:
        complete_task(tasks)
        save_tasks(tasks)

    elif choice == 6:
        search_task(tasks)

    elif choice == 7:
        print("Exiting Task Manager...")
        break

    else:
        print("Invalid choice!")