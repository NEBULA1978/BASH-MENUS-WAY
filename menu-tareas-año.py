tasks = {}


def add_task(date, task):
    if date not in tasks:
        tasks[date] = []
    tasks[date].append({"task": task, "completed": False})
    print("Task added successfully!")


def mark_task_completed(date, task_index):
    tasks[date][task_index]["completed"] = True
    print("Task marked as completed!")


def print_pending_tasks():
    print("Pending tasks:")
    for date in tasks:
        for index, task in enumerate(tasks[date]):
            if not task["completed"]:
                print(f"{date}: [{index+1}] {task['task']}")


def print_completed_tasks(tasks):
    print("Tareas completadas:")
    for task, date in tasks.items():
        if date != None:
            print(f"\t- {task} ({date})")

# Example usage
add_task("2023-04-27", "Buy groceries")
add_task("2023-04-27", "Do laundry")
add_task("2023-04-28", "Submit report")
add_task("2023-04-30", "Attend meeting")
mark_task_completed("2023-04-27", 0)
print_pending_tasks()
