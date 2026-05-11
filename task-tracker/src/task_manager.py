from models import Task
from storage import load_tasks, save_tasks

def add_task(title:str) -> None:
    tasks = load_tasks()
    tasks.append(Task(title=title))
    save_tasks(tasks)