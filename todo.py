# To-Do List Project - Updated by Venu``
import os

TASK_FILE = "tasks.txt"

# Load tasks from file
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            return [task.strip() for task in file.readlines()]
    return []

# Save tasks to file
def save_tasks():
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

tasks = load_tasks()  # Load tasks when program starts

def show_menu():
    print("\n📌 To-Do List Menu:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def view_tasks():
    if not tasks:
        print("📭 No tasks found!")
    else:
        print("\n📝 Your Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks()
        print(f"✅ Task '{task}' added successfully!")
    else:
        print("⚠️ Task cannot be empty!")

def remove_task():
    view_tasks()
    if not tasks:
        return
    try:
        task_no = int(input("Enter task number to remove: "))
        removed_task = tasks.pop(task_no - 1)
        save_tasks()
        print(f"❌ Task '{removed_task}' removed!")
    except (ValueError, IndexError):
        print("⚠️ Invalid number. Try again.")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("👋 Exiting To-Do List. Have a great day!")
            break
        else:
            print("⚠️ Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main()
