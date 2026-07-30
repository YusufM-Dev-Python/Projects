# Define a function to display the current tasks in the to-do list
def show_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is currently empty.")
    else:
        print("\n--- Current To-Do List ---")
        # Use enumerate to display each task with its corresponding index number starting from 1
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")


# Define the main to-do list application function to handle user interaction and control flow
def todo_app():
    # Initialize an empty list to store the tasks
    tasks = []

    print("--- Terminal-Based To-Do List Application ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Quit")

    # Start a continuous loop to keep the application running until the user decides to quit
    while True:
        # Prompt the user to select an option and remove any trailing/leading whitespace
        choice = input(
            "\nEnter choice (1/2/3/4) or type 'q' to quit: "
        ).strip()

        # Check if the user wants to exit the application
        if choice.lower() == "q" or choice == "4":
            print("Exiting To-Do List Application. Goodbye!")
            break

        # Option 1: View all tasks using enumerate
        if choice == "1":
            show_tasks(tasks)

        # Option 2: Add a new task to the list
        elif choice == "2":
            new_task = input("Enter the task description: ").strip()
            if new_task:
                tasks.append(new_task)
                print(f"Success: '{new_task}' added to your list.")
            else:
                print("Error: Task description cannot be empty.")

        # Option 3: Delete an existing task using conditional logic and index validation
        elif choice == "3":
            if not tasks:
                print("\nYour to-do list is empty, nothing to delete.")
                continue

            show_tasks(tasks)
            task_input = input(
                "Enter the task number you want to delete: "
            ).strip()

            # Check if the input consists only of digits to avoid errors without using try-except
            if task_input.isdigit():
                task_num = int(task_input)
                # Check if the entered number matches a valid index in the list
                if 1 <= task_num <= len(tasks):
                    # Remove the task using its zero-based index equivalent
                    removed_task = tasks.pop(task_num - 1)
                    print(f"Success: Removed '{removed_task}' from your list.")
                else:
                    print(
                        "Error: Invalid task number. Please choose a number from the list."
                    )
            else:
                print("Invalid input. Please enter a valid number.")

        else:
            # Handle out-of-range choices
            print(
                "Invalid Choice. Please select a valid option between 1 and 4."
            )


# Ensure the to-do application runs only when the script is executed directly
if __name__ == "__main__":
    todo_app()