# To-Do List Application using Python

# List to store tasks
tasks = []

def show_menu():
    print("\n--------- TO-DO LIST MENU ---------")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")
    print("-----------------------------------")

# Display tasks
def view_tasks():
    if len(tasks) == 0:
        print("\nNo tasks available.")
    else:
        print("\nYour Tasks:")
        for index, task in enumerate(tasks, start=1):
            status = "✓ Completed" if task['done'] else "✗ Pending"
            print(f"{index}. {task['title']} - {status}")

# Add a new task
def add_task():
    title = input("\nEnter task name: ")
    tasks.append({"title": title, "done": False})
    print("Task added successfully!")

# Mark task as completed
def complete_task():
    view_tasks()
    try:
        task_no = int(input("\nEnter task number to mark completed: "))
        tasks[task_no - 1]['done'] = True
        print("Task updated successfully!")
    except:
        print("Invalid task number!")

# Delete a task
def delete_task():
    view_tasks()
    try:
        task_no = int(input("\nEnter task number to delete: "))
        removed = tasks.pop(task_no - 1)
        print(f"Deleted: {removed['title']}")
    except:
        print("Invalid task number!")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting program... Goodbye!")
        break
    else:
        print("Invalid choice! Please enter 1-5.")
