import json
from datetime import datetime

class Task:
    def __init__(self, task_id, description, created_at, priority):
        self.id = task_id
        self.description = description
        self.created_at = created_at
        self.priority = priority
    

class TaskManager:
    def __init__(self, file_path="tasks.txt"):
        self.file_path = file_path
        self.tasks = self.load_tasks()
    
    def load_tasks(self):
        pass
    def save_tasks(self):
        pass

    def add_task(self, description, priority):
        pass

    def delete_task(self, task_id):
        pass

    def list_tasks(self, sort_by="priority"):
        pass

    def complete_task(self, task_id):
        pass