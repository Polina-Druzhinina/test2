from src.models import Task

def test_task_creation() -> None:
    task = Task(title="Test task")

    assert task.title == "Test task"
    assert task.completed is False