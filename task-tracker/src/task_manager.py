from src.models import Task
from src.storage import load_tasks, save_tasks


class TaskNotFoundError(Exception):
    pass


def add_task(title: str) -> None:
    tasks = load_tasks()
    tasks.append(Task(title=title))
    save_tasks(tasks)


def list_tasks() -> None:
    tasks = load_tasks()
    if not tasks:
        raise TaskNotFoundError("No tasks found")
    for index, task in enumerate(tasks, start=1):
        status = "ok" if task.completed else " "
        print(f"[{status}] {index}.{task.title}")


def complete_task(index: int) -> None:
    tasks = load_tasks()
    if index < 1 or index > len(tasks):
        raise TaskNotFoundError("Invalid task index")
    tasks[index - 1].completed = True
    save_tasks(tasks)
