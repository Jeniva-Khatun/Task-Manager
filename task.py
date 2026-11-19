
class Task:
    def __init__(self,id,title,description,priority,status):
        self.id = id
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status
        pass

# Creating Task Objects

task1 = Task(1, "Learn Python", "Study OOP", "High", "Pending")    
task2 = Task(2, "Practice DSA", "Solve array problems", "Medium", "Pending")


# Display Task 1
print("\n--- Task 1 ---")
print("Task ID:", task1.id)
print("Title:", task1.title)
print("Description:", task1.description)
print("Priority:", task1.priority)
print("Status:", task1.status)


# Display Task 2
print("\n--- Task 2 ---")
print("Task ID:", task2.id)
print("Title:", task2.title)
print("Description:", task2.description)
print("Priority:", task2.priority)
print("Status:", task2.status)

# Update Task 1 status
task1.status = "Completed"
print("\n--- Updated Task 1 ---")
print("Status:", task1.status)



# Update Task 2 priority
task2.priority = "High"
print("\n--- Updated Task 2 ---")
print("Priority:", task2.priority)
