
# todo_list_manager.py
# Command-Line To-Do Manager — saves to tasks.json and loads on start.
import json
from datetime import datetime, timedelta

FILE_NAME = "tasks.json"

def load_tasks():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)

def add_task(tasks):
    desc = input("Task description: ").strip()
    due = input("Due date YYYY-MM-DD (optional): ").strip()
    status = "Pending"
    tasks.append({"description": desc, "due_date": due, "status": status})
    save_tasks(tasks); print("Added ✔")

def list_tasks(tasks, filter_by=None):
    now = datetime.now()
    print("\n#  Description                     Due Date    Status")
    shown = 0
    for i, t in enumerate(tasks, 1):
        if filter_by == "completed" and t["status"] != "Completed": 
            continue
        if filter_by == "pending" and t["status"] == "Completed":
            continue
        if filter_by == "due-soon":
            if not t["due_date"]:
                continue
            try:
                d = datetime.strptime(t["due_date"], "%Y-%m-%d")
            except ValueError:
                continue
            if not (now <= d <= now + timedelta(days=3)):
                continue
        print(f"{i:>2} {t['description'][:28]:<28}  {t['due_date'] or '-':<10}  {t['status']}")
        shown += 1
    if shown == 0:
        print("(no tasks to show)")

def edit_task(tasks):
    list_tasks(tasks)
    if not tasks: return
    try:
        idx = int(input("Enter # to edit: ")) - 1
        t = tasks[idx]
    except (ValueError, IndexError):
        print("Invalid selection."); return
    print("Leave blank to keep existing value.")
    new_desc = input(f"Description [{t['description']}]: ").strip()
    new_due = input(f"Due YYYY-MM-DD [{t['due_date'] or ''}]: ").strip()
    new_status = input(f"Status (Pending/Completed) [{t['status']}]: ").strip()
    if new_desc: t["description"] = new_desc
    if new_due: t["due_date"] = new_due
    if new_status in {"Pending","Completed"}: t["status"] = new_status
    save_tasks(tasks); print("Updated ✔")

def mark_complete(tasks):
    list_tasks(tasks, "pending")
    if not tasks: return
    try:
        idx = int(input("Enter # to mark complete: ")) - 1
        tasks[idx]["status"] = "Completed"
        save_tasks(tasks); print("Marked Completed ✔")
    except (ValueError, IndexError):
        print("Invalid selection.")

def delete_task(tasks):
    list_tasks(tasks)
    if not tasks: return
    try:
        idx = int(input("Enter # to delete: ")) - 1
        tasks.pop(idx); save_tasks(tasks); print("Deleted ✔")
    except (ValueError, IndexError):
        print("Invalid selection.")

def menu():
    tasks = load_tasks()
    while True:
        print("\n=== To-Do List Manager ===")
        print("1) Add task")
        print("2) View all tasks")
        print("3) View completed")
        print("4) View pending")
        print("5) View due soon (≤3 days)")
        print("6) Mark task complete")
        print("7) Edit task")
        print("8) Delete task")
        print("9) Exit")
        ch = input("Choose: ").strip()
        if ch == "1": add_task(tasks)
        elif ch == "2": list_tasks(tasks)
        elif ch == "3": list_tasks(tasks, "completed")
        elif ch == "4": list_tasks(tasks, "pending")
        elif ch == "5": list_tasks(tasks, "due-soon")
        elif ch == "6": mark_complete(tasks)
        elif ch == "7": edit_task(tasks)
        elif ch == "8": delete_task(tasks)
        elif ch == "9": print("Bye!"); break
        else: print("Invalid option.")

if __name__ == "__main__":
    menu()
