class Task:
    task_counter = 0

    def __init__(self, description, priority):
        Task.task_counter += 1
        self.task_id = Task.task_counter
        self.description = description
        self.priority = priority
        self.completed = False

    def mark_completed(self):
        self.completed = True


class PriorityQueue:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        self.tasks.sort(key=lambda x: x.priority, reverse=True)

    def get_highest_priority_task(self):
        if self.tasks:
            return self.tasks[0]
        else:
            return None

    def mark_completed_and_enqueue(self):
        if self.tasks:
            task = self.tasks.pop(0)
            task.mark_completed()
            return task
        else:
            return None


class Stack:
    def __init__(self):
        self.tasks = []

    def push(self, task):
        self.tasks.append(task)

    def pop(self):
        if self.tasks:
            return self.tasks.pop()
        else:
            return None


class TaskManager:
    def __init__(self):
        self.task_queue = PriorityQueue()
        self.task_history = Stack()

    def add_task(self, description, priority):
        task = Task(description, priority)
        self.task_queue.add_task(task)

    def get_task(self, task_id):
        for task in self.task_queue.tasks:
            if task.task_id == task_id:
                return task
        return None

    def display_all_tasks(self):
        for task in self.task_queue.tasks:
            print(f"Task {task.task_id}: {task.description} (Priority: {task.priority}, Completed: {task.completed})")

    def display_incomplete_tasks(self):
        incomplete_tasks = [task for task in self.task_queue.tasks if not task.completed]
        for task in incomplete_tasks:
            print(f"Task {task.task_id}: {task.description} (Priority: {task.priority}, Completed: {task.completed})")

    def display_last_completed_task(self):
        last_completed_task = self.task_history.pop()
        if last_completed_task:
            print(f"Last Completed Task: {last_completed_task.description}")
        else:
            print("No completed tasks in history.")

    def menu(self):
        while True:
            print("\nTask Manager Menu:")
            print("1. Add a new task")
            print("2. Get a task by ID")
            print("3. Mark highest priority task as completed")
            print("4. Display all tasks in order of priority")
            print("5. Display only incomplete tasks")
            print("6. Display last completed task")
            print("7. Exit")

            choice = input("Enter your choice (1-7): ")

            if choice == '1':
                description = input("Enter task description: ")
                priority = int(input("Enter task priority: "))
                self.add_task(description, priority)
            elif choice == '2':
                task_id = int(input("Enter task ID: "))
                task = self.get_task(task_id)
                if task:
                    print(f"Task {task_id}: {task.description} (Priority: {task.priority}, Completed: {task.completed})")
                else:
                    print(f"No task found with ID {task_id}")
            elif choice == '3':
                completed_task = self.task_queue.mark_completed_and_enqueue()
                if completed_task:
                    self.task_history.push(completed_task)
                    print(f"Task {completed_task.task_id} marked as completed.")
                else:
                    print("No tasks to mark as completed.")
            elif choice == '4':
                self.display_all_tasks()
            elif choice == '5':
                self.display_incomplete_tasks()
            elif choice == '6':
                self.display_last_completed_task()
            elif choice == '7':
                print("Exiting Task Manager. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    manager = TaskManager()
    manager.menu()
