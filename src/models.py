from dataclasses import dataclass, field
from datetime import datetime
import uuid

@dataclass
class TodoItem:
    """Todo task model with all necessary fields"""
    title: str
    description: str = ""
    completed: bool = False
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
    
    def to_dict(self):
        """Convert task to dictionary"""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
            "created_at": self.created_at.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create task from dictionary"""
        return cls(
            id=data["id"],
            title=data["title"],
            description=data.get("description", ""),
            completed=data["completed"],
            created_at=datetime.fromisoformat(data["created_at"])
        )