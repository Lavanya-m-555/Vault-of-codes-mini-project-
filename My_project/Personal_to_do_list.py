import json

# Task class
class Task:
    def __init__(self, title, description, category):
        self.title = title
        self.description = description
        self.category = category
        self.completed = False

    def mark_completed(self):
        self.completed = True

# Save tasks to file
def save_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump([task.__dict__ for task in tasks], f, indent=4)

# Load tasks from file
def load_tasks():
    try:
        with open('tasks.json', 'r') as f:
            return [Task(**data) for data in json.load(f)]
    except FileNotFoundError:
        return []

# Display all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    for i, task in enumerate(tasks, start=1):
        status = "✔️ Completed" if task.completed else "❌ Pending"
        print(f"{i}. {task.title} - {task.description} [{task.category}] ({status})")

# Main program
def main():
    tasks = load_tasks()
    while True:
        print("\n--- Personal To-Do List ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            category = input("Enter task category (Work/Personal/Urgent): ")
            tasks.append(Task(title, description, category))
            save_tasks(tasks)
            print("✅ Task added successfully!")

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            view_tasks(tasks)
            task_num = int(input("Enter task number to mark completed: ")) - 1
            if 0 <= task_num < len(tasks):
                tasks[task_num].mark_completed()
                save_tasks(tasks)
                print("✅ Task marked as completed!")

        elif choice == "4":
            view_tasks(tasks)
            task_num = int(input("Enter task number to delete: ")) - 1
            if 0 <= task_num < len(tasks):
                tasks.pop(task_num)
                save_tasks(tasks)
                print("🗑️ Task deleted successfully!")

        elif choice == "5":
            save_tasks(tasks)
            print("👋 Exiting... Tasks saved!")
            break

        else:
            print("❌ Invalid choice, try again.")

if __name__ == "__main__":
    main()
