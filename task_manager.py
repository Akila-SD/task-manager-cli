import json
DUMMY_EMAIL = "testuser@example.com"
DUMMY_PASSWORD = "password123"
class Task:
    def __init__(self, id, title, completed=False):
        self.id = id
        self.title = title
        self.completed = completed
    def __str__(self):
        status = "Completed" if self.completed else "Not Completed"
        return f"ID: {self.id}, Title: {self.title}, Status: {status}"
def add_task(tasks, title):
    task_id = len(tasks) + 1
    task = Task(task_id, title)
    tasks.append(task)
    print(f"Task '{title}' added with ID {task_id}.")
def view_tasks(tasks):
    if tasks:
        print("\nTasks List:")
        for task in tasks:
            print(task)
    else:
        print("No tasks available.")
def delete_task(tasks, task_id):
    task_to_delete = next((task for task in tasks if task.id == task_id), None)
    if task_to_delete:
        tasks.remove(task_to_delete)
        print(f"Task with ID {task_id} deleted.")
    else:
        print(f"Task with ID {task_id} not found.")
def mark_task_complete(tasks, task_id):
    task_to_mark = next((task for task in tasks if task.id == task_id), None)
    if task_to_mark:
        task_to_mark.completed = True
        print(f"Task with ID {task_id} marked as completed.")
    else:
        print(f"Task with ID {task_id} not found.")
def save_tasks(tasks, filename='tasks.json'):
    with open(filename, 'w') as file:
        json.dump([task.__dict__ for task in tasks], file)
    print("Tasks saved to file.")
def load_tasks(filename='tasks.json'):
    try:
        with open(filename, 'r') as file:
            tasks_data = json.load(file)
            return [Task(**task) for task in tasks_data]
    except FileNotFoundError:
        return []
def show_menu():
    print("\nTask Manager Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Complete")
    print("5. Save Tasks")
    print("6. Load Tasks")
    print("7. Exit")
def login():
    print("Welcome to Task Manager CLI Application")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    if email == DUMMY_EMAIL and password == DUMMY_PASSWORD:
        print("Login successful! Welcome!")
        return True
    else:
        print("Invalid email or password. Please try again.")
        return False
def main():
    if login():
        tasks = load_tasks()
        while True:
            show_menu()
            choice = input("Choose an option (1-7): ")

            if choice == '1':
                title = input("Enter task title: ")
                add_task(tasks, title)
            elif choice == '2':
                view_tasks(tasks)
            elif choice == '3':
                task_id = int(input("Enter task ID to delete: "))
                delete_task(tasks, task_id)
            elif choice == '4':
                task_id = int(input("Enter task ID to mark complete: "))
                mark_task_complete(tasks, task_id)
            elif choice == '5':
                save_tasks(tasks)
            elif choice == '6':
                tasks = load_tasks()
                print("Tasks loaded from file.")
            elif choice == '7':
                save_tasks(tasks)
                print("Exiting the program. Tasks saved.")
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Access denied. Exiting the application.")
if __name__ == "__main__":
    main()