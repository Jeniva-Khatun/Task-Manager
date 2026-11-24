

from datetime import datetime,date
from input_validation import validate_title, validate_priority
from database import insert_task, get_all_tasks



def add_task():
    print("\n===== ADD NEW TASK =====")

    title = validate_title()
    description = input("Enter task description: ")
    priority = validate_priority()

    while True:
        date_input = input("Enter due date (YYYY-MM-DD): ")

        try:
            due_date = datetime.strptime(date_input, "%Y-%m-%d").date()
            break

        except ValueError:
            print("Invalid date! Please use YYYY-MM-DD.")

    status = "Pending"

    insert_task(title, description, priority, status, str(due_date))

    print("\nTask added successfully!")

def view_tasks():

    print("\n===== YOUR TASKS =====")

    tasks = get_all_tasks()
    today = date.today()

    if not tasks:
        print("No task available")
        return

    for task in tasks:

        due_date = None

        if task[5] is not None:
             try:
                due_date = date.fromisoformat(task[5])
             except ValueError:
               print("\nInvalid date stored in database!")
        
        

        print("\nTask ID:", task[0])
        print("Title:", task[1])
        print("Description:", task[2])
        print("Priority:", task[3])
        print("Status:", task[4])
        print("Due Date:", task[5])

        # Check whether the task is overdue
        if due_date is not None and due_date < today and task[4] != "Completed":
            print("Deadline: OVERDUE")

        elif task[4] == "Completed":
            print("Deadline: COMPLETED")


                       


