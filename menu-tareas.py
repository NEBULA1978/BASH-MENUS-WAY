tasks = {}
completed_tasks = {}


def add_task():
    task_name = input("Enter task name: ")
    task_date = input("Enter task date (dd/mm/yyyy): ")
    tasks[task_name] = task_date
    print("Task added successfully.")


def mark_as_completed():
    task_name = input("Enter task name: ")
    if task_name in tasks:
        completed_tasks[task_name] = tasks[task_name]
        del tasks[task_name]
        print("Task marked as completed.")
    else:
        print("Task not found.")


def print_pending_tasks():
    print("Pending tasks:")
    for task, date in tasks.items():
        print(f"{task} - {date}")


def print_completed_tasks():
    print("Completed tasks:")
    for task, date in completed_tasks.items():
        print(f"{task} - {date}")


while True:
    print("\nMenu:")
    print("1. Add task")
    print("2. Mark task as completed")
    print("3. Print pending tasks")
    print("4. Print completed tasks")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        mark_as_completed()
    elif choice == "3":
        print_pending_tasks()
    elif choice == "4":
        print_completed_tasks()
    elif choice == "5":
        break
    else:
        print("Invalid choice.")

# This is a Python program that allows the user to add pending tasks for each day, month, and year, and mark them as completed. The program uses a dictionary to store tasks and their dates, with functions to add tasks, mark them as completed, and print pending tasks. The user can also see completed tasks by selecting a new option from the menu that calls a function to print completed tasks. The program will continue to run until the user chooses to exit.

# Este es un programa de Python que permite al usuario agregar tareas pendientes para cada día, mes y año, y marcarlas como completadas. El programa utiliza un diccionario para almacenar tareas y sus fechas, con funciones para agregar tareas, marcarlas como completadas e imprimir tareas pendientes. El usuario también puede ver las tareas completadas seleccionando una nueva opción del menú que llama a una función para imprimir tareas completadas. El programa seguirá ejecutándose hasta que el usuario decida salir.
