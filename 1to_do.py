class TodoList:
    def __init__(self):
        # The constructor method initializes a new TodoList object with an empty list of tasks.
        self.tasks = []

    def add_task(self, task):
        # This method adds a task to the tasks list.
        self.tasks.append(task)

    def remove_task(self, index):
        # This method removes a task from the tasks list at the given index if the index is valid.
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            print("Task removed successfully!")
        else:
            print("Invalid task index. Please try again.")

    def display_tasks(self):
        # This method prints all the tasks in the tasks list.
        if self.tasks:
            print("Your To-Do List:")
            for i, task in enumerate(self.tasks):
                print(f"{i+1}. {task}")
        else:
            print("Your To-Do List is empty")

    def update_task(self, index, new_task):
        # This method updates the task at the given index with a new task if the index is valid.
        if 0 <= index < len(self.tasks):
            self.tasks[index] = new_task
            print("Task updated successfully!")
        else:
            print("Invalid task index. Please try again.")

def main():
    # Create an instance of TodoList.
    todo_list = TodoList()

    while True:
        # Print the menu options for the user.
        print("\n===== To-Do List Menu =====")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Update Task")
        print("4. Display Tasks")
        print("5. Exit")

        # Prompt the user to enter their choice.
        choice = input("Enter your choice: ")

        if choice == '1':
            # If the user chooses to add a task, prompt for the task description and add it.
            task = input("Enter task to add: ")
            todo_list.add_task(task)
        elif choice == '2':
            # If the user chooses to remove a task, prompt for the task index and remove it.
            index = int(input("Enter task index to remove: ")) - 1
            todo_list.remove_task(index)
        elif choice == '3':
            # If the user chooses to update a task, prompt for the task index and the new task description and update it.
            index = int(input("Enter task index to update: ")) - 1
            new_task = input("Enter new task: ")
            todo_list.update_task(index, new_task)
        elif choice == '4':
            # If the user chooses to display all tasks, display them.
            todo_list.display_tasks()
        elif choice == '5':
            # If the user chooses to exit, break out of the loop.
            print("Exiting program.")
            break
        else:
            # If the user enters an invalid choice, print an error message.
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    # Run the main function if the script is executed directly.
    main()
