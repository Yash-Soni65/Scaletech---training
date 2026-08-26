import csv

def save_tasks(tasks, filename="tasks.csv"):
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["name", "time", "completed"]
        )

        writer.writeheader()
        writer.writerows(tasks)