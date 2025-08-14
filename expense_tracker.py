
# expense_tracker.py
# Personal Expense Tracker — saves to expenses.json and loads on start.
import json
from datetime import datetime
from collections import defaultdict

FILE_NAME = "expenses.json"

def load_expenses():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_expenses(expenses):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(expenses, f, indent=2, ensure_ascii=False)

def prompt_amount():
    while True:
        try:
            return float(input("Enter amount (e.g., 75.50): ").strip())
        except ValueError:
            print("Invalid number. Try again.")

def prompt_date():
    raw = input("Enter date YYYY-MM-DD (Enter for today): ").strip()
    if not raw:
        return datetime.now().strftime("%Y-%m-%d")
    try:
        datetime.strptime(raw, "%Y-%m-%d")
        return raw
    except ValueError:
        print("Invalid date. Using today.")
        return datetime.now().strftime("%Y-%m-%d")

def add_expense(expenses):
    print("\n— Add Expense —")
    amount = prompt_amount()
    category = input("Enter category (Food, Transport, Rent, etc.): ").strip() or "Misc"
    date = prompt_date()
    note = input("Optional note: ").strip()
    expenses.append({"amount": amount, "category": category, "date": date, "note": note})
    save_expenses(expenses)
    print("Saved ✔\n")

def list_expenses(expenses):
    if not expenses:
        print("No expenses yet.")
        return
    print("\n#  Date        Category        Amount   Note")
    for i, e in enumerate(expenses, 1):
        print(f"{i:>2} {e['date']:>10}  {e['category']:<14}  ₹{e['amount']:>7.2f}  {e.get('note','')}")

def edit_expense(expenses):
    list_expenses(expenses)
    if not expenses: return
    try:
        idx = int(input("Enter # to edit: ")) - 1
        e = expenses[idx]
    except (ValueError, IndexError):
        print("Invalid selection."); return
    print("Leave blank to keep existing value.")
    new_amt = input(f"Amount [{e['amount']}]: ").strip()
    new_cat = input(f"Category [{e['category']}]: ").strip()
    new_date = input(f"Date YYYY-MM-DD [{e['date']}]: ").strip()
    new_note = input(f"Note [{e.get('note','')}]: ").strip()
    if new_amt:
        try: e['amount'] = float(new_amt)
        except: print("Amount unchanged.")
    if new_cat: e['category'] = new_cat
    if new_date:
        try: datetime.strptime(new_date, "%Y-%m-%d"); e['date'] = new_date
        except: print("Date unchanged.")
    if new_note: e['note'] = new_note
    save_expenses(expenses); print("Updated ✔\n")

def delete_expense(expenses):
    list_expenses(expenses)
    if not expenses: return
    try:
        idx = int(input("Enter # to delete: ")) - 1
        removed = expenses.pop(idx)
        save_expenses(expenses)
        print(f"Deleted {removed['category']} ₹{removed['amount']} on {removed['date']} ✔\n")
    except (ValueError, IndexError):
        print("Invalid selection.")

def summary_overall(expenses):
    total = sum(e['amount'] for e in expenses)
    print(f"\nTotal spent: ₹{total:.2f}")
    by_cat = defaultdict(float)
    for e in expenses:
        by_cat[e['category']] += e['amount']
    print("By category:")
    for k, v in sorted(by_cat.items(), key=lambda x: -x[1]):
        print(f"  {k}: ₹{v:.2f}")

def summary_over_time(expenses, period="daily"):
    from datetime import datetime
    key_fn = None
    if period == "daily":
        key_fn = lambda d: d.strftime("%Y-%m-%d")
    elif period == "weekly":
        iso = lambda d: d.isocalendar()
        key_fn = lambda d: f"{iso(d).year}-W{iso(d).week:02d}"
    elif period == "monthly":
        key_fn = lambda d: d.strftime("%Y-%m")
    else:
        print("Unknown period."); return
    buckets = defaultdict(float)
    for e in expenses:
        try:
            d = datetime.strptime(e['date'], "%Y-%m-%d")
        except ValueError:
            continue
        buckets[key_fn(d)] += e['amount']
    print(f"\nSpending by {period}:")
    for k, v in sorted(buckets.items()):
        print(f"  {k}: ₹{v:.2f}")

def menu():
    expenses = load_expenses()
    while True:
        print("\n=== Personal Expense Tracker ===")
        print("1) Add expense")
        print("2) List expenses")
        print("3) Edit expense")
        print("4) Delete expense")
        print("5) Summary (overall/category)")
        print("6) Summary over time (daily/weekly/monthly)")
        print("7) Exit")
        choice = input("Choose: ").strip()
        if choice == "1": add_expense(expenses)
        elif choice == "2": list_expenses(expenses)
        elif choice == "3": edit_expense(expenses)
        elif choice == "4": delete_expense(expenses)
        elif choice == "5": summary_overall(expenses)
        elif choice == "6":
            p = input("Period [daily/weekly/monthly]: ").strip().lower() or "daily"
            summary_over_time(expenses, p)
        elif choice == "7":
            print("Bye!"); break
        else: print("Invalid option.")

if __name__ == "__main__":
    menu()
