
tasks = []


def add_task():
    task_name = input("Enter task: ").strip()

    if task_name:
        task = {
            "title": task_name,
            "completed": False
        }

        tasks.append(task)
        print("Task added successfully.\n")
    else:
        print("Task cannot be empty.\n")


def view_tasks():
    if not tasks:
        print("No tasks available.\n")
        return

    print("\n------ TO-DO LIST ------")

    for index, task in enumerate(tasks, start=1):
        status = "✓ Completed" if task["completed"] else "✗ Pending"
        print(f"{index}. {task['title']} [{status}]")

    print()


def mark_completed():
    view_tasks()

    if not tasks:
        return

    try:
        task_number = int(input("Enter task number to mark completed: "))

        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
            print("Task marked as completed.\n")
        else:
            print("Invalid task number.\n")

    except ValueError:
        print("Please enter a valid number.\n")


def delete_task():
    view_tasks()

    if not tasks:
        return

    try:
        task_number = int(input("Enter task number to delete: "))

        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Deleted: {removed_task['title']}\n")
        else:
            print("Invalid task number.\n")

    except ValueError:
        print("Please enter a valid number.\n")


def main():
    while True:
        print("========== TO-DO LIST ==========")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            mark_completed()

        elif choice == "4":
            delete_task()

        elif choice == "5":
            print("Thank you for using To-Do List App.")
            break

        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()