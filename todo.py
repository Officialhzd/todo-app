import os
from datetime import datetime
from storage import load_tasks, save_tasks, get_today_key
from rich.console import Console
from rich.table import Table

console = Console()

def validate_date(d: str) -> bool:
    """
    Validate if the given string is a valid date in YYYY-MM-DD format.
    """
    try:
        datetime.strptime(d, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def add_task():
    """
    Add a new task to the to-do list.
    """
    all_tasks = load_tasks()
    day = get_today_key()
    tasks = all_tasks.get(day, [])

    while True:
        title = input("Task Title (required): ").strip().title()
        if title:
            break
        console.print("[red]Task title is required. Please try again.[/]")

    description = input("Task Description (optional): ").strip()

    due = ""
    while True:
        due_in = input("Due Date (YYYY‑MM‑DD, optional): ").strip()
        if due_in == "" or validate_date(due_in):
            due = due_in
            break
        console.print("[red]Invalid date format.[/]")

    task = {
        "ID": chr(len(tasks) % 26 + ord("A")) + ("" if len(tasks) < 26 else chr(len(tasks) // 26 - 1 + ord("A"))),
        "Title": title,
        "Description": description,
        "Due_Date": due,
        "Status": "Pending"
    }
    tasks.append(task)
    all_tasks[day] = tasks
    save_tasks(all_tasks)
    console.print(f"[green]Task added:[/] {title}")

def view_tasks():
    """
    View all tasks in the to-do list.
    """
    all_tasks = load_tasks()
    if not all_tasks:
        console.print("[yellow]No tasks found.[/]")
        return

    for day, tasks in all_tasks.items():
        console.print(f"\n[bold underline]Tasks for {day}[/]")
        table = Table(show_lines=True)
        table.add_column("ID")
        table.add_column("Title")
        table.add_column("Description")
        table.add_column("Due")
        table.add_column("Status")
        for t in tasks:
            due = t["Due_Date"] or "Today"
            if due != "-" and validate_date(due):  # Check if the due date is valid
                d = datetime.strptime(due, "%Y-%m-%d")
                if d < datetime.today():
                    due += " ⚠️"  # Add a warning if the due date is in the past
            table.add_row(
                t["ID"],
                t["Title"],
                t["Description"] or "-",  # Show "-" if no description is provided
                due,
                t["Status"]
            )
        console.print(table)

def delete_task():
    """
    Delete a task or all tasks for a specific day.
    """
    all_tasks = load_tasks()
    day = input("Enter date (YYYY‑MM‑DD) to delete from (leave blank for today): ").strip() or get_today_key()
    tasks = all_tasks.get(day, [])
    if not tasks:
        console.print(f"[red]No tasks on {day}[/]")
        return

    choice = input("Delete [1] single task or [2] all tasks for this day? ")
    if choice == "2":
        all_tasks.pop(day)
        save_tasks(all_tasks)
        console.print(f"[green]All tasks on {day} removed[/]")
        return

    tid = input("Enter Task ID to delete: ").strip().upper()
    task_found = False
    new_tasks = []
    for t in tasks:
        if t["ID"] == tid:
            task_found = True
        else:
            new_tasks.append(t)

    if not task_found:
        console.print("[red]Task ID not found[/]")
    else:
        all_tasks[day] = new_tasks
        save_tasks(all_tasks)
        console.print(f"[green]Task {tid} deleted[/]")

def complete_task():
    """
    Mark a task as completed.
    """
    all_tasks = load_tasks()
    day = input("Enter date (YYYY‑MM‑DD) of task (blank=today): ").strip() or get_today_key()
    tasks = all_tasks.get(day, [])
    if not tasks:
        console.print(f"[red]No tasks on {day}[/]")
        return

    tid = input("Enter Task ID to mark complete: ").strip().upper()
    for t in tasks:
        if t["ID"] == tid:
            t["Status"] = "Completed"
            save_tasks(all_tasks)
            console.print(f"[green]{t['Title']} marked completed[/]")
            return
    console.print("[red]Task not found[/]")

def edit_tasks():
    """
    Edit a task's details.
    """
    all_tasks = load_tasks()
    day = input("Enter date (YYYY‑MM‑DD) of task (blank=today): ").strip() or get_today_key()
    tasks = all_tasks.get(day, [])
    tid = input("Enter Task ID to edit: ").upper()
    for t in tasks:
        if t["ID"] == tid:
            console.print(f"Editing [bold]{t['Title']}[/]")
            new_title = input(f"New Title ({t['Title']}): ").strip()
            if new_title: t["Title"] = new_title
            new_desc = input(f"New Desc ({t['Description']}): ").strip()
            if new_desc: t["Description"] = new_desc
            while True:
                nd = input(f"New Due ({t['Due_Date']}): ").strip()
                if nd == "" or validate_date(nd):
                    t["Due_Date"] = nd; break
                console.print("[red]Bad date[/]")
            save_tasks(all_tasks)
            console.print("[green]Task updated[/]")
            return
    console.print("[red]Task not found[/]")
