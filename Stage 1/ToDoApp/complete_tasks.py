def mark_task_completed(tasks, task_id):
    if 0 < task_id <= len(tasks):
        tasks[task_id - 1]['completed'] = True
        print(f"Task ID '{task_id}' marked as completed.")
    else:
        print("Invalid task ID.")
