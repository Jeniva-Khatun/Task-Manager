
# import json
 

# tasks = [
#      {
#         "id": 1,
#         "title": "Learn Python",
#         "description": "Practice Python concepts",
#         "priority": "High",
#         "status": "Pending"
#     },
#     {
#         "id": 2,
#         "title": "Build Task Manager",
#         "description": "Complete Day 6",
#         "priority": "Medium",
#         "status": "Pending"print("ID:", task["id"])
#     print("Title:", task["title"])
#     print("Priority:", task["priority"])
#     print("Status:", task["status"])
#     print("--------------------")
#     },
#     {
#         "id": 3,
#         "title": "Practice SQL",
#         "description": "Learn database queries",
#         "priority": "Low",
#         "status": "Completed"
#     }


# ]
# # Convert Python dictionary into JSON string
# json_data = json.dumps(tasks)

# # Display JSON data
# print(json_data)

# # Save tasks into JSON file  #json.dump() → Saves data into a JSON file.
# with open("tasks.json", "w") as file:
#     json.dump(tasks,file, indent = 4)

# print("Tasks saved successfully!")

# # Load tasks from JSON file
# with open("tasks.json", "r") as file:
#     loaded_tasks = json.load(file)


# # Display loaded tasks
# print("\nLoaded Tasks:")

# for task in loaded_tasks:
#     print("ID:", task["id"])
#     print("Title:", task["title"])
#     print("Priority:", task["priority"])
#     print("Status:", task["status"])
#     print("--------------------")

import json
import os

# Load tasks from JSON file
def load_tasks():

    if not os.path.exists("tasks.json"):
        print("No previous tasks found.")
        return []

    with open("tasks.json", "r") as file:
        tasks = json.load(file)

    print("Tasks loaded successfully!")
    return tasks


# Save tasks into JSON file
def save_tasks(tasks):

    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

    print("Tasks saved successfully!")   
    print("File location:", os.path.abspath("tasks.json")) 