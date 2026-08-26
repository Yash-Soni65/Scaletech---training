def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("\n== Tasks ==")

        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task['name']}")
            print(f"   Created at: {task['time']}")
            print(f"   Status: {'Completed' if task['completed'] else 'Pending'}")
