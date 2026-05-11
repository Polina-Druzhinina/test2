from models import Task
from storage import load_tasks, save_tasks

def add_task(title:str) -> None:
    tasks = load_tasks()
    tasks.append(Task(title=title))
    save_tasks(tasks)

def list_task() -> None:
    tasks = load_tasks()
    if not tasks:
        print("No tasks found")
        return
    for index, task in enumerate(tasks, start=1):
        status = "ok" if task.completed else " "
        print(f"[{status}] {index}.{task.title}")

def complete_task(index: int) -> None:
    tasks = load_tasks()
    if index < 1 or index > len(tasks):
        print("Invalid task index")
        return
    tasks[index-1].completed = True
    save_tasks(tasks)