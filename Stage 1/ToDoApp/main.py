from save_tasks import save_tasks
from update_tasks import update_task
from view_tasks import view_tasks
from complete_tasks import mark_task_completed
from add_tasks import add_task
from delete_tasks import delete_task
from load_tasks import load_tasks

tasks = load_tasks()

while True:

    print("\n== To-Do List App ==")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as completed")
    print("4. Update a task")
    print("5. Delete a task")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":

        add_task(tasks)
        save_tasks(tasks)

    elif choice == "2":

        view_tasks(tasks)

    elif choice == "3":

        task_id = int(input("Enter the task ID to mark as completed: "))

        mark_task_completed(tasks, task_id)
        save_tasks(tasks)

    elif choice == "4":

        task_id = int(input("Enter the task ID to update: "))

        update_task(tasks, task_id)
        save_tasks(tasks)

    elif choice == "5":

        task_id = int(input("Enter the task ID to delete: "))

        delete_task(tasks, task_id)
        save_tasks(tasks)
    elif choice == "6":

        print("Exiting the To-Do List App.")
        break
    else:

        print("Invalid choice.")