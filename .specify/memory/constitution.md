
# Todo App Made Constitution

## Project Overview
**Name:** Todo App Made  
**Type:** CLI-based Task Management Application  
**Language:** Python  
**Architecture:** Modular, layered architecture with separation of concerns

## Core Principles

### I. Simple CRUD Operations
Every feature should revolve around the core actions: Create, Read, Update, and Delete. We prioritize straightforward implementations over complex abstractions. If a feature doesn't directly support or enhance these core operations, its necessity must be justified.

**Implementation Details:**
- `add` - Create new tasks with title and optional description
- `list` - Display all tasks in a readable format
- `update` - Modify existing task properties
- `toggle` - Mark tasks as complete/incomplete
- `delete` - Remove tasks permanently
- `exit` - Close application gracefully

### II. Data Persistence (Reliability First)
User data is sacred. Every change must be immediately and safely persisted to storage (`tasks.json`). The application must ensure that no data is lost during transitions, updates, or unexpected exits. Serialization and deserialization logic should be robust and backward-compatible.

**Implementation:**
- Storage: `tasks.json` in project root
- Auto-save on every operation
- Atomic writes to prevent corruption
- Data validation before saving
- Graceful handling of corrupted files

### III. Clean Code & Maintainability
We follow the principles of "Simple Code." This means:

**Modular Architecture:**
- `models.py` - Task data model (TodoItem class)
- `storage.py` - File I/O operations (load/save tasks)
- `service.py` - Business logic (task operations)
- `cli.py` - User interface layer (menu, input handling)
- `main.py` - Application entry point

**Naming Conventions:**
- Clear, descriptive names (`task_list` not `tl`)
- Functions do one thing well
- Maximum 3 levels of nesting

**Dependencies:**
- Minimal dependencies to keep project lightweight
- Standard library preferred over third-party packages

### IV. User Experience (UX) First
The CLI interface must be intuitive and responsive. Inputs should be validated, and helpful feedback (success messages or clear error descriptions) must be provided for every action. We aim for a "zero-learning-curve" experience for the user.

**UX Guidelines:**
- Numbered menu options (1-6)
- Clear prompts for user input
- Success confirmations for all operations
- Helpful error messages (not technical stack traces)
- Consistent formatting of task lists
- Exit confirmation to prevent accidental data loss

### VI. Operation History & Auditing
To ensure transparency and recoverability, all significant operations (Add, Update, Delete) must be logged. This history serves as an audit trail and a foundation for Undo/Redo functionality.

**Implementation:**
- Maintain a history log (e.g., in a `history/` directory or distinct file).
- Log the type of operation, timestamp, and the data affected.
- Ensure history logging does not impact the performance of core operations.

## Technology Stack

**Core:**
- Python 3.8+
- JSON for data storage
- Standard library only (no external dependencies for MVP)

**Development Tools:**
- VS Code with Python extension
- Git for version control
- Speckit for AI-assisted development

**File Structure:**
```
todo_app_made/
├── src/
│   ├── __init__.py
│   ├── main.py         # Entry point
│   ├── cli.py          # CLI interface
│   ├── models.py       # Data models
│   ├── service.py      # Business logic
│   └── storage.py      # File operations
├── .specify/           # Speckit configuration
│   ├── memory/
│   │   └── constitution.md
│   └── commands/
├── tasks.json          # Data file (generated)
├── README.md
└── requirements.txt    # (if needed)
```

## Data Model

**TodoItem:**
```python
{
    "id": "unique_identifier",
    "title": "Task title",
    "description": "Optional description",
    "completed": false,
    "created_at": "2026-01-02T18:30:00",
    "updated_at": "2026-01-02T18:30:00"
}
```

## Development Workflow

1. **Feature Planning**
   - Define clear requirements
   - Check constitution compliance
   - Plan which file(s) to modify

2. **Implementation**
   - Update models if data structure changes
   - Add/modify service layer functions
   - Update CLI interface
   - Test manually

3. **Testing**
   - Run all CRUD operations
   - Check tasks.json for data integrity
   - Test error scenarios

4. **Commit**
   - Clear commit messages: "Add task priority feature"
   - Commit working code only

## AI Development Guidelines

When using Gemini/Claude with Speckit:
- Always reference: "Follow Todo App Made constitution"
- Ask AI to explain changes before implementing
- Review generated code for constitution compliance
- Test AI-generated features thoroughly

## Quality Standards

**Performance:**
- All operations complete in < 100ms
- No lag in menu display

**Reliability:**
- Zero data loss
- Graceful error handling
- File corruption recovery

**Usability:**
- Maximum 3 clicks/inputs for any operation
- No cryptic error messages
- Intuitive menu flow

## Feature Roadmap

**MVP (Current):**
- ✅ Add tasks
- ✅ List tasks
- ✅ Update tasks
- ✅ Toggle completion
- ✅ Delete tasks
- ✅ Persistent storage

**Planned Enhancements:**
1. Task priorities (High/Medium/Low)
2. Due dates
3. Task categories/tags
4. Search/filter functionality
5. Export to CSV
6. Undo/Redo operations

## Governance

- This constitution guides ALL development decisions
- Code reviews must verify constitution compliance
- Complexity requires strong justification
- When in doubt: **Simple > Complex**
- Update this document when project evolves

**Amendment Process:**
1. Identify need for change
2. Document reason and impact
3. Update constitution
4. Notify team/update README
5. Increment version number

---

**Version:** 1.1.0  
**Ratified:** 2026-01-02  
**Last Amended:** 2026-01-02  
**Maintained By:** Development Team  
**Review Cycle:** Monthly or after major features.
