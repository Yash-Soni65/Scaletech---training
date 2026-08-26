import csv

def load_tasks(filename="tasks.csv"):
    tasks = []

    try:
        with open(filename, "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                row["completed"] = row["completed"] == "True"
                tasks.append(row)

    except FileNotFoundError:
        print("No existing tasks found. Starting with an empty list.")

    return tasks