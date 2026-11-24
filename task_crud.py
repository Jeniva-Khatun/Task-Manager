
from input_validation import validate_title, validate_task_id

from database import (
    get_all_tasks,
    update_task as update_task_in_db,
    delete_tasks as delete_task_in_db,
    complete_task as complete_task_in_db,
    search_tasks_by_title, filter_tasks,
    get_sorted_tasks
)


def update_task():
    tasks = get_all_tasks()

    if not tasks:
        print("No tasks available!")
        return

    task_id = validate_task_id()

    new_title = validate_title()

    update_task_in_db(task_id, new_title)


def delete_task():
    tasks = get_all_tasks()

    if not tasks:
        print("No tasks available!")
        return

    task_id = validate_task_id()

    delete_task_in_db(task_id)


def complete_task():
    tasks = get_all_tasks()

    if not tasks:
        print("No tasks available!")
        return

    task_id = validate_task_id()

    complete_task_in_db(task_id)



def search_task():
    print("\n===== SEARCH TASK =====")

    keyword = input("Enter task title or keyword: ")

    tasks = search_tasks_by_title(keyword)

    if not tasks:
        print("No matching tasks found!")
        return

    for task in tasks:
        print("\nTask ID:", task[0])
        print("Title:", task[1])
        print("Description:", task[2])
        print("Priority:", task[3])
        print("Status:", task[4])
        print("Due Date:", task[5])


def filter_task():
    print("\n===== FILTER TASKS =====")
    print("1. Filter by Status")
    print("2. Filter by Priority")
    print("3. Filter by Both")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        status = input(
            "Enter status (Pending/Completed): "
        ).strip().title()

        tasks = filter_tasks(status=status)

    elif choice == "2":
        priority = input(
            "Enter priority (High/Medium/Low): "
        ).strip().title()

        tasks = filter_tasks(priority=priority)

    elif choice == "3":
        status = input(
            "Enter status (Pending/Completed): "
        ).strip().title()

        priority = input(
            "Enter priority (High/Medium/Low): "
        ).strip().title()

        tasks = filter_tasks(
            status=status,
            priority=priority
        )

    else:
        print("Invalid choice!")
        return

    if not tasks:
        print("No matching tasks found!")
        return

    print("\n===== FILTERED TASKS =====")

    for task in tasks:
        print("\nTask ID:", task[0])
        print("Title:", task[1])
        print("Description:", task[2])
        print("Priority:", task[3])
        print("Status:", task[4])
        print("Due Date:", task[5])        



def sort_task():
    print("\n===== SORT TASKS =====")
    print("1. Sort by Due Date")
    print("2. Sort by Priority")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        tasks = get_sorted_tasks("due_date")

    elif choice == "2":
        tasks = get_sorted_tasks("priority")

    else:
        print("Invalid choice!")
        return

    if not tasks:
        print("No tasks available!")
        return

    print("\n===== SORTED TASKS =====")

    for task in tasks:
        print("\nTask ID:", task[0])
        print("Title:", task[1])
        print("Description:", task[2])
        print("Priority:", task[3])
        print("Status:", task[4])
        print("Due Date:", task[5])

    


    
   
    
