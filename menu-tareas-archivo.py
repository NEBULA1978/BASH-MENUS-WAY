import os

tasks = {}


def add_task():
    date = input("Enter the date (dd/mm/yyyy): ")
    task = input("Enter the task: ")
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = [task]
    print("Task added successfully.")


def complete_task():
    date = input("Enter the date (dd/mm/yyyy) of the task you completed: ")
    if date in tasks:
        print("Pending tasks for", date)
        for task in tasks[date]:
            print("- ", task)
        task_index = int(input("Enter the index of the completed task: "))
        completed_task = tasks[date].pop(task_index)
        if "completed_tasks" in tasks:
            tasks["completed_tasks"].append((date, completed_task))
        else:
            tasks["completed_tasks"] = [(date, completed_task)]
        print("Task marked as completed.")
    else:
        print("No tasks found for that date.")


def print_pending_tasks():
    print("Pending tasks:")
    for date, tasks_list in tasks.items():
        for task in tasks_list:
            print("- ", date, task)


def print_completed_tasks():
    if "completed_tasks" in tasks:
        print("Completed tasks:")
        for date, completed_task in tasks["completed_tasks"]:
            print("- ", date, completed_task)
    else:
        print("No completed tasks yet.")


def write_to_file():
    with open("resultados.txt", "w") as f:
        f.write("Pending tasks:\n")
        for date, tasks_list in tasks.items():
            for task in tasks_list:
                f.write("- " + date + " " + task + "\n")
    print("Pending tasks written to resultados.txt")


def write_completed_tasks():
    if "completed_tasks" in tasks:
        with open("tareas-realizadas.txt", "w") as f:
            f.write("Completed tasks:\n")
            for date, completed_task in tasks["completed_tasks"]:
                f.write("- " + date + " " + completed_task + "\n")
        print("Completed tasks written to tareas-realizadas.txt")
    else:
        print("No completed tasks yet.")


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def menu():
    while True:
        clear_screen()
        print("1. Add task")
        print("2. Complete task")
        print("3. Print pending tasks")
        print("4. Print completed tasks")
        print("5. Write pending tasks to file")
        print("6. Write completed tasks to file")
        print("7. Exit")

        option = input("Enter your option: ")

        if option == "1":
            add_task()
        elif option == "2":
            complete_task()
        elif option == "3":
            print_pending_tasks()
        elif option == "4":
            print_completed_tasks()
        elif option == "5":
            write_to_file()
        elif option == "6":
            write_completed_tasks()
        elif option == "7":
            print("Goodbye!")
            break
        else:
            input("Invalid option. Press Enter to try again.")


if __name__ == "__main__":
    menu()
