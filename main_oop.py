
from task import Task
from task_manager import TaskManager

# Step 1: Create TaskManager object
manager = TaskManager()

# Step 2: Create Task objects
task1 = Task(1, "Learn Python", "Study OOP", "High", "Pending")

task2 = Task(2, "Practice DSA", "Solve array problems", "Medium", "Pending")

# Step 3: Add tasks to TaskManager
manager.add_task(task1)
manager.add_task(task2)
manager.display_tasks()
