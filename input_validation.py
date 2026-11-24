
def validate_title():
    while True:
        title = input("Enter the title: ")

        if not title.strip():
            print("Error: Title cannot be empty !")
        else:
            print("valid title !") 
            return title.strip()

def validate_priority():
    valid_priorities = ["high", "medium", "low"]

    while True:
        priority = input("Enter priority (High/Medium/Low): ").strip().lower()

        if priority in valid_priorities:
            print("Valid priority!")
            return priority.capitalize()
        else:
            print("Error: Invalid priority! Choose High, Medium or Low.")        


def validate_task_id():
    while True:
        try:
            task_id = int(input("Enter task ID : "))

            if task_id <= 0:
                print("Error : Task ID must be positive! ")
            else:
                print("Valid task ID!") 
                return task_id 
            
        except ValueError:
            print("Error: Task ID must be a number!")

def task_exists(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            return True

    return False
    

#testing----------------
if __name__ == "__main__":

    tasks = [
        {"id": 1, "title": "Learn Python"},
        {"id": 2, "title": "Practice SQL"}
    ]

    print("\n--- Title Validation ---")
    title = validate_title()
    print("Your task : ", title) 

    print("\n--- ID Validation ---")
    task_id = validate_task_id()
    print("Your task ID : ", task_id)

    print("\n--- Task Existence Check ---")
    if task_exists(tasks, task_id):
        print("Task Found !")
    else:
        print("Task NOT Found!")    







           
