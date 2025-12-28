from .models import TodoItem
from .storage import TaskStorage

class TodoService:
    def __init__(self, storage: TaskStorage):
        self.storage = storage
    
    def create_task(self, title: str, description: str = ""):
        """Create a new task"""
        task = TodoItem(title=title, description=description)
        self.storage.add(task)
        return task
    
    def list_tasks(self):
        """Get all tasks"""
        return self.storage.get_all()
    
    def get_task(self, task_id: str):
        """Get a specific task by ID"""
        return self.storage.get(task_id)
    
    def update_task(self, task_id: str, title: str = None, description: str = None):
        """Update task title or description"""
        return self.storage.update(task_id, title, description)
    
    def delete_task(self, task_id: str):
        """Delete a task"""
        return self.storage.delete(task_id)
    
    def toggle_task(self, task_id: str):
        """Toggle task completion status"""
        return self.storage.toggle_complete(task_id)
