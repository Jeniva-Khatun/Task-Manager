

def add_task(tasks):
    print("\n===== ADD NEW TASK =====")

    title = input("Enter task title: ")
    description = input("Enter task description: ")
    task_id = len(tasks) + 1


    task = {
        "id": task_id,
        "title": title,
        "description": description,
        "status": "Pending"
    }
    tasks.append(task)

    print("\nTask added successfully!")

def view_tasks(tasks):
        
        print("\n===== YOUR TASKS =====")

        if len(tasks) ==0:
                print("No task available")

        else:
               for task in tasks:
                      print("\nTask ID: ", task["id"])
                      print("Title: ",task["title"])
                      print("Description:", task["description"])
                      print("Status:", task["status"])

                       

  

