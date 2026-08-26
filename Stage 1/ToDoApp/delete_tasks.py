def delete_task(tasks, task_id):
    if 0 < task_id <= len(tasks):
        deleted_task = tasks.pop(task_id - 1)
        print(f"Task '{deleted_task}' deleted.")
    else:
        print("Invalid task ID.")
