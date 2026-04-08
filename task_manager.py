import json
from datetime import datetime

class Task:
    def __init__(self, task_id, description, created_at, priority):
        self.id = task_id
        self.description = description
        self.created_at = created_at
        self.priority = priority

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "created_at": self.created_at,
            "priority": self.priority
        }
    
class TaskManager:
    def __init__(self, file_path="tasks.txt"):
        self.file_path = file_path
        self.tasks = self.load_tasks()
    
    def load_tasks(self):
        try:
            with open(self.file_path, "r") as file:
                tasks_data = json.load(file)
                return [Task(**task) for task in tasks_data]
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open(self.file_path, "w") as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def add_task(self, description, priority, created_at):
        if priority < 1 or priority > 5:
            raise ValueError("Приорітет має бути між 1 та 5")

        try:
            datetime.strptime(created_at, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Дата має бути в форматі YYYY-MM-DD")

        task_id = len(self.tasks) + 1
        task = Task(task_id, description, created_at, priority)
        self.tasks.append(task)
        self.save_tasks()

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.id != task_id]
        self.save_tasks()

    def list_tasks(self, sort_by="priority"):
        pass

    def complete_task(self, task_id):
        pass