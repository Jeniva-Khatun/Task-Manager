from task_operation import add_task, view_tasks

tasks =[]
print(tasks)

while True:
    print("\n===== PYTHON TASK MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_task(tasks)

    elif choice == 2:
        view_tasks(tasks)

    elif choice == 3:
        print("Exiting Task Manager...")  
        break
     
    else:
        print("Invalid choice")     

