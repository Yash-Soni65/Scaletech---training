from datetime import datetime
def add_task(tasks):
    task_name = input("Enter the task name: ")
    task = {"name": task_name,
            "time": datetime.now().strftime("%d-%m-%y %H:%M:%S"),
            "completed": False}
    tasks.append(task)
    print(f"Task '{task['name']}' added.")