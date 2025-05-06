from todo import add_task, view_tasks, edit_tasks, complete_task, delete_task
from rich.console import Console

console = Console()

def main():
    while True:
        console.print("\n[bold blue]── To‑Do List App ──[/]")
        console.print("1. Add Task    2. View Tasks    3. Edit Task")
        console.print("4. Complete    5. Delete    6. Exit")
        choice = input("Choose: ").strip()
        match choice:
            case "1": add_task()
            case "2": view_tasks()
            case "3": edit_tasks()
            case "4": complete_task()
            case "5": delete_task()
            case "6":
                console.print("[bold green]Goodbye![/]")
                break
            case _:
                console.print("[red]Invalid choice. Please try again.[/]")

if __name__ == "__main__":
    main()