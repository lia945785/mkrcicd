import pytest
from datetime import datetime
from task_manager import TaskManager  


@pytest.fixture
def manager(tmp_path):
    test_file = tmp_path / "test_tasks.json"
    return TaskManager(file_path=str(test_file))

def test_add_task_success(manager):
    manager.add_task("Купити хліб", 1, "2026-04-08")
    assert len(manager.tasks) == 1
    assert manager.tasks[0].description == "Купити хліб"
    assert manager.tasks[0].priority == 1

@pytest.mark.parametrize("priority", [1, 2, 3, 4, 5])
def test_valid_priorities(manager, priority):
    manager.add_task("Task", priority, "2026-04-08")
    assert manager.tasks[-1].priority == priority

@pytest.mark.parametrize("invalid_priority", [0, 6, -1, 10])
def test_invalid_priority_raises_error(manager, invalid_priority):
    with pytest.raises(ValueError, match="Приорітет має бути між 1 та 5"):
        manager.add_task("Bad Task", invalid_priority, "2026-04-08")


def test_invalid_date_format(manager):
    with pytest.raises(ValueError, match="Дата має бути в форматі YYYY-MM-DD"):
        manager.add_task("Task", 1, "08-04-2026") 

def test_delete_task(manager):
    manager.add_task("Task to delete", 1, "2026-04-08")
    task_id = manager.tasks[0].id
    manager.delete_task(task_id)
    assert len(manager.tasks) == 0

def test_complete_task(manager):
    manager.add_task("Finish project", 1, "2026-04-08")
    task_id = manager.tasks[0].id
    manager.complete_task(task_id)
    assert len(manager.tasks) == 0

def test_sort_by_priority(manager):
    manager.add_task("Low priority", 5, "2026-04-08")
    manager.add_task("High priority", 1, "2026-04-08")
    
    sorted_tasks = manager.list_tasks(sort_by="priority")
    assert sorted_tasks[0].priority == 1
    assert sorted_tasks[1].priority == 5

def test_sort_by_date(manager):
    manager.add_task("Later task", 1, "2026-05-10")
    manager.add_task("Earlier task", 1, "2026-04-01")
    
    sorted_tasks = manager.list_tasks(sort_by="date")
    assert sorted_tasks[0].created_at == "2026-04-01"
    assert sorted_tasks[1].created_at == "2026-05-10"