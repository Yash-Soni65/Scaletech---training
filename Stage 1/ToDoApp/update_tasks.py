
def update_task(tasks, task_id):
    if 0 < task_id <= len(tasks):
        new_name = input("Enter new task name: ")

        tasks[task_id - 1]["name"] = new_name

        print(f"Task ID '{task_id}' updated.")
    else:
        print("Invalid task ID.")