
class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1


    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    def display_tasks(self):
        if not self.tasks:
            print("No Task available ")
            return

        print("=== All TASKS ===")
        for task in self.tasks:
            print(f"\n Task ID : {task.id}" ) 
            print(f"Title: {task.title}")
            print(f"Priority: {task.priority}")
            print(f"Status: {task.status}") 


    def find_task(self, task_id):

        for task in self.tasks:
            if task.id == task_id :
                return task
        return None        
