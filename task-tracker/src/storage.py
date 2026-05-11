import json
from pathlib import Path
from src.models import Task

DATA_FILE = Path("data/tasks.json")

def load_tasks() -> list[Task]:
    if not DATA_FILE.exists():
        return []
    data = json.loads(DATA_FILE.read_text())
    return [Task(**item) for item in data]

def save_tasks(tasks: list[Task]) -> None:
    DATA_FILE.parent.mkdir(exist_ok=True)
    data = [
        {
            "title": task.title,
            "completed": task.completed,
        }
        for task in tasks
    ]

    DATA_FILE.write_text(json.dumps(data, indent=4))

