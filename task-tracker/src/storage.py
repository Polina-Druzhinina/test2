import json
from pathlib import Path
from models import Task

DATA_FILE = Path("data/tasks.json")

def load_tasks() -> list[Task]:
    if not DATA_FILE.exists():
        return []
    data = json.loads(DATA_FILE.read_text())
    return [Task(**item) for item in data]

