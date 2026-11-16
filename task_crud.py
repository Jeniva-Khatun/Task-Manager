# tasks = [
#     {
#         "id": 1,
#         "title": "Learn Python",
#         "description": "Study dictionaries",
#         "status": "Pending"
#     },
#     {
#         "id": 2,
#         "title": "Practice SQL",
#         "description": "Learn SQL queries",
#         "status": "Pending"
#     }
# ]

def update_task(tasks):
    if not tasks:
        print("No tasks available!")
        return

    task_id = int(input("Enter Task ID: "))

    for task in tasks:
        if task["id"] == task_id:
            new_title = input("Enter new title: ")
            task["title"] = new_title
            print("Task updated successfully!")
            break
    else:
        print("Task not found!")   


def delete_task(tasks):
    if not tasks:
        print("No tasks available!")
        return

    task_id = int(input("Enter Task ID: "))

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            print("Task deleted successfully!")
            break
    else:
        print("Task not found!")


def complete_task(tasks):
    if not tasks:
        print("No tasks available!")
        return

    task_id = int(input("Enter Task ID: "))

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "Completed"
            print("Task marked as completed!")
            break
    else:
        print("Task not found!")


def search_task(tasks):
    if not tasks:
        print("No tasks available!")
        return

    task_id = int(input("Enter Task ID: "))

    for task in tasks:
        if task["id"] == task_id:
            print("\n===== TASK DETAILS =====")
            print("ID:", task["id"])
            print("Title:", task["title"])
            print("Description:", task["description"])
            print("Status:", task["status"])
            break
    else:
        print("Task not found!")


