from input_validation import validate_title , validate_task_id, task_exists

def update_task(tasks):
    if not tasks:
        print("No tasks available!")
        return

    task_id = validate_task_id()

    for task in tasks:
        if task["id"] == task_id:
            new_title = validate_title()
            task["title"] = new_title
            print("Task updated successfully!")
            break
    else:
        print("Task not found!")   


def delete_task(tasks):
    if not tasks:
        print("No tasks available!")
        return

    task_id = validate_task_id()

    if not task_exists(tasks, task_id):
        print("Task not found!")
        return

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

    task_id = validate_task_id()

    if not task_exists(tasks, task_id):
        print("Task not found!")
        return


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

    task_id = validate_task_id()

    if not task_exists(tasks, task_id):
        print("Task not found!")
        return

    for task in tasks:
        if task["id"] == task_id:
            print("\n===== TASK DETAILS =====")
            print("ID:", task["id"])
            print("Title:", task["title"])
            print("Description:", task["description"])
            print("Status:", task["status"])
            return 
    

