
task = {
    "id" : 1 ,
    "title" :"Learn Python" ,
    "description" :"Complete python basic",
    "priority" :"High",
    "status" :" Pending" 
}

print("Task Title : ", task["title"])
print("Priority : ", task["priority"])
print("Status : ", task["status"])

task["status"] = "Completed"
print("Updated status : ", task["status"])

task["title"] ="Built Task Manager"
print("Updated Title : ", task["title"])

task["priority"] ="Low"
print("Updated Priority : ", task["priority"])