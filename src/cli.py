import sys
from .service import TodoService
from .storage import TaskStorage

def print_menu():
    print("\n--- Todo App ---")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Update Task")
    print("4. Toggle Complete")
    print("5. Delete Task")
    print("6. Exit")
    print("----------------")

def main():
    storage = TaskStorage()
    service = TodoService(storage)
    
    while True:
        print_menu()
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            title = input("Enter title: ").strip()
            if not title:
                print("Title cannot be empty.")
                continue
            desc = input("Enter description (optional): ").strip()
            task = service.create_task(title, desc)
            print(f"Task created with ID: {task.id}")
        
        elif choice == "2":
            tasks = service.list_tasks()
            if not tasks:
                print("No tasks found.")
            else:
                for t in tasks:
                    status = "[x]" if t.completed else "[ ]"
                    print(f"{status} {t.id} - {t.title}: {t.description}")
        
        elif choice == "3":
            task_id = input("Enter Task ID to update: ").strip()
            title = input("New title (press enter to keep current): ").strip()
            desc = input("New description (press enter to keep current): ").strip()
            
            # Convert empty strings to None for the service
            title = title if title else None
            desc = desc if desc else None
            
            if service.update_task(task_id, title, desc):
                print("Task updated successfully.")
            else:
                print("Task not found.")
        
        elif choice == "4":
            task_id = input("Enter Task ID to toggle: ").strip()
            if service.toggle_task(task_id):
                print("Task status updated.")
            else:
                print("Task not found.")
        
        elif choice == "5":
            task_id = input("Enter Task ID to delete: ").strip()
            if service.delete_task(task_id):
                print("Task deleted.")
            else:
                print("Task not found.")
        
        elif choice == "6":
            print("Goodbye!")
            break
        
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
