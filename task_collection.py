
tasks = [
    {
        "id":1,
        "title":"Learn Python",
        "priority":"High",
        "status":"Pending",
    },
    {
        "id":2,
        "title":"Practice Coding",
        "priority":"Medium",
        "status":"Completed", 
    },
    {
        "id":3,
        "title":"Build Task Manager",
        "priority":"High",
        "status":"Pending", 
    }
]

def display_tasks(tasks):
        print("----- MY TASKS -----")

        for task in tasks:
             print("ID:", task["id"])
             print("Title:", task["title"])
             print("Priority:", task["priority"])
             print("Status:", task["status"])
             print()
          
display_tasks(tasks)    

def count_tasks(tasks):
       print("Total Tasks : ", len(tasks))

count_tasks(tasks)
print()

print("----Pending Tasks----")
for task in tasks:
       if(task["status"]=="Pending" ):
              print(task["title"])
print()

print("\n----- UPDATING TASK -----")
for task in tasks:
       if task["id"]==1:
              task["status"]="Completed"
              print("Updated status : ", task["status"])
print("Task updated successfully")             
display_tasks(tasks)                        

      
