import json
import os
from .models import TodoItem

class TaskStorage:
    def __init__(self, file_path="tasks.json"):
        self.file_path = file_path
        self.tasks = self._load_tasks()
    
    def _load_tasks(self):
        if not os.path.exists(self.file_path):
            return []
        try:
            with open(self.file_path, "r") as f:
                data = json.load(f)
                return [TodoItem.from_dict(item) for item in data]
        except (json.JSONDecodeError, KeyError):
            return []
    
    def _save_tasks(self):
        with open(self.file_path, "w") as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=4)
    
    def add(self, task: TodoItem):
        self.tasks.append(task)
        self._save_tasks()
    
    def get(self, task_id: str):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
    
    def get_all(self):
        return self.tasks
    
    def update(self, task_id: str, title: str = None, description: str = None):
        task = self.get(task_id)
        if task:
            if title is not None:
                task.title = title
            if description is not None:
                task.description = description
            self._save_tasks()
            return True
        return False
    
    def delete(self, task_id: str):
        original_length = len(self.tasks)
        self.tasks = [t for t in self.tasks if t.id != task_id]
        if len(self.tasks) < original_length:
            self._save_tasks()
            return True
        return False
    
    def toggle_complete(self, task_id: str):
        task = self.get(task_id)
        if task:
            task.completed = not task.completed
            self._save_tasks()
            return True
        return False
