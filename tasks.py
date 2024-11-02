import os
import sys
import json
import time

# Handle user input
def get_user_input():
    """
    Retrieves user input from the command line arguments or prompts the user for input.
    If a command line argument is provided, it is used as the user input.
    Otherwise, a welcome message is displayed and the user is prompted to enter a command.
    Returns:
        str: The user input command.
    """
    
    if len(sys.argv) > 1:
        user_input = sys.argv[1]
    else:
        print("Welcome to the task manager")
        print("Try 'add', 'update', 'delete' or 'list'")
        user_input = input("What would you like to do?: \n")
    return user_input

# Database creation function
def database_creation():
    """
    Creates a JSON file named 'tasks-database.json' if it does not already exist.
    
    The JSON file will contain an empty dictionary with a key "tasks".
    """
    if not os.path.exists('tasks-database.json'):
        with open('tasks-database.json', 'w') as f:
            json.dump({"tasks": {}}, f, indent=4)

# Generate a unique task ID
def generate_task_id():
    """
    Generates a new unique task ID based on the existing tasks in the 'tasks-database.json' file.
    The function reads the 'tasks-database.json' file to get the current tasks. If there are no tasks,
    it returns "1" as the first task ID. Otherwise, it finds the maximum existing task ID, increments it by one,
    and returns it as a string.
    Returns:
        str: A new unique task ID.
    """
    
    with open('tasks-database.json', 'r') as f:
        data = json.load(f)
        if not data["tasks"]:
            return "1"
        return str(max(map(int, data["tasks"].keys())) + 1)

# Add a task
def add_task():
    """
    Prompts the user to input a task description, generates a unique task ID, and adds the task to the tasks-database.json file.
    The task is stored with the following attributes:
    - description: The task description provided by the user.
    - status: The status of the task, initially set to "open".
    - created_at: The timestamp when the task was created.
    - updated_at: The timestamp when the task was last updated (initially the same as created_at).
    The function reads the existing tasks from tasks-database.json, adds the new task, and writes the updated tasks back to the file.
    Raises:
        FileNotFoundError: If the tasks-database.json file does not exist.
        json.JSONDecodeError: If the tasks-database.json file contains invalid JSON.
    Prints:
        A success message with the generated task ID.
    """
    
    task = input("What task would you like to add?: \n")
    task_id = generate_task_id()
    status = "open"
    created_at = time.strftime("%Y-%m-%d %H:%M:%S")
    updated_at = time.strftime("%Y-%m-%d %H:%M:%S")
    
    task_data = {
        "description": task,
        "status": status,
        "created_at": created_at,
        "updated_at": updated_at
    }
    
    with open('tasks-database.json', 'r') as f:
        data = json.load(f)
        data["tasks"][task_id] = task_data
    
    with open('tasks-database.json', 'w') as f:
        json.dump(data, f, indent=4)
    
    print(f"Task added successfully with ID {task_id}")

# Add a test task
def add_test_task():
    """
    Adds a test task to the tasks-database.json file.
    This function creates a test task with a description "Test task", generates a unique task ID,
    sets the status to "open", and records the current time as both the creation and update time.
    The task is then added to the tasks-database.json file.
    Raises:
        FileNotFoundError: If the tasks-database.json file does not exist.
        json.JSONDecodeError: If there is an error decoding the JSON data from the file.
    Prints:
        A success message with the task ID of the newly added test task.
    """
    
    task = "Test task"
    task_id = generate_task_id()
    status = "open"
    created_at = time.strftime("%Y-%m-%d %H:%M:%S")
    updated_at = time.strftime("%Y-%m-%d %H:%M:%S")
    
    task_data = {
        "description": task,
        "status": status,
        "created_at": created_at,
        "updated_at": updated_at
    }
    
    with open('tasks-database.json', 'r') as f:
        data = json.load(f)
        data["tasks"][task_id] = task_data
    
    with open('tasks-database.json', 'w') as f:
        json.dump(data, f, indent=4)
    
    print(f"Test task added successfully with ID {task_id}")

def update_task():
    """
    Prompts the user to update a task's description and status in the tasks-database.json file.
    The function performs the following steps:
    1. Prompts the user to input the task ID they want to update.
    2. Prompts the user to input the new task description.
    3. Prompts the user to input the new status of the task.
    4. Reads the current tasks from the tasks-database.json file.
    5. If the new task description is not provided, retains the existing description.
    6. Updates the task's description, status, and updated_at timestamp if the task ID exists.
    7. Writes the updated tasks back to the tasks-database.json file.
    8. Prints a success message if the task is updated, otherwise prints "Task not found."
    Note:
    - The tasks-database.json file should be in the same directory as this script.
    - The task ID should be a valid key in the tasks dictionary within the JSON file.
    """
    
    task_id = input("What task would you like to update?: \n")
    new_task = input("What is the new task description?: \n")
    new_status = input("What is the new status?: \n")
    updated_at = time.strftime("%Y-%m-%d %H:%M:%S")
    
    with open('tasks-database.json', 'r') as f:
        data = json.load(f)
        if not new_task:
            new_task = data["tasks"][task_id]["description"]
        if task_id in data["tasks"]:
            data["tasks"][task_id]["description"] = new_task
            data["tasks"][task_id]["status"] = new_status
            data["tasks"][task_id]["updated_at"] = updated_at
        else:
            print("Task not found.")
    
    with open('tasks-database.json', 'w') as f:
        json.dump(data, f, indent=4)
    
    print(f"Task with ID {task_id} updated successfully")

def delete_task():
    """
    Prompts the user to input the ID of the task they wish to delete, 
    then removes the task from the 'tasks-database.json' file if it exists.
    The function performs the following steps:
    1. Prompts the user to enter the task ID.
    2. Reads the 'tasks-database.json' file to load existing tasks.
    3. Checks if the entered task ID exists in the tasks.
    4. If the task ID exists, deletes the task from the data.
    5. Writes the updated task data back to the 'tasks-database.json' file.
    6. Prints a success message if the task was deleted, or a "Task not found" message if the task ID does not exist.
    Raises:
        FileNotFoundError: If the 'tasks-database.json' file does not exist.
        json.JSONDecodeError: If the 'tasks-database.json' file is not a valid JSON.
    """

    task_id = input("What task would you like to delete?: \n")
    
    with open('tasks-database.json', 'r') as f:
        data = json.load(f)
        if task_id in data["tasks"]:
            del data["tasks"][task_id]
        else:
            print("Task not found.")
    
    with open('tasks-database.json', 'w') as f:
        json.dump(data, f, indent=4)
    
    print(f"Task with ID {task_id} deleted successfully")

def delete_all_tasks():
    """
    Deletes all tasks from the tasks-database.json file.
    This function reads the tasks-database.json file, clears all tasks by setting the "tasks" key to an empty dictionary,
    and then writes the updated data back to the file. A success message is printed upon completion.
    """
    
    with open('tasks-database.json', 'r') as f:
        data = json.load(f)
        data["tasks"] = {}
    
    with open('tasks-database.json', 'w') as f:
        json.dump(data, f, indent=4)
    
    print("All tasks deleted successfully")

def list_tasks():
    """
    Lists all tasks from the tasks-database.json file.
    This function reads the tasks from the 'tasks-database.json' file and prints
    each task's ID, description, status, creation date, and last updated date.
    If no tasks are found, it prints a message indicating that no tasks are available.
    Raises:
        FileNotFoundError: If the 'tasks-database.json' file does not exist.
        json.JSONDecodeError: If the file is not a valid JSON.
    """
    
    with open('tasks-database.json', 'r') as f:
        data = json.load(f)
        if not data["tasks"]:
            print("No tasks found.")
        else:
            for task_id, task_data in data["tasks"].items():
                print(f"Task ID: {task_id}")
                print(f"Description: {task_data['description']}")
                print(f"Status: {task_data['status']}")
                print(f"Created at: {task_data['created_at']}")
                print(f"Updated at: {task_data['updated_at']}")
                print("\n")

def show_task():
    """
    Prompts the user to input a task ID and displays the details of the task if it exists in the tasks-database.json file.
    The function reads the tasks-database.json file, checks if the provided task ID exists in the "tasks" dictionary,
    and prints the task details including description, status, created_at, and updated_at. If the task ID does not exist,
    it prints "Task not found."
    Raises:
        FileNotFoundError: If the tasks-database.json file does not exist.
        json.JSONDecodeError: If the tasks-database.json file is not a valid JSON.
    """
    
    task_id = input("What task would you like to see?: \n")
    
    with open('tasks-database.json', 'r') as f:
        data = json.load(f)
        if task_id in data["tasks"]:
            print(f"Task ID: {task_id}")
            print(f"Description: {data['tasks'][task_id]['description']}")
            print(f"Status: {data['tasks'][task_id]['status']}")
            print(f"Created at: {data['tasks'][task_id]['created_at']}")
            print(f"Updated at: {data['tasks'][task_id]['updated_at']}")
        else:
            print("Task not found.")

def filter_tasks():
    """
    Prompts the user to input a status and filters tasks from a JSON database
    based on the provided status. The function reads tasks from 'tasks-database.json'
    and prints the details of tasks that match the specified status.
    The details printed for each matching task include:
    - Task ID
    - Description
    - Status
    - Created at timestamp
    - Updated at timestamp
    Raises:
        FileNotFoundError: If the 'tasks-database.json' file does not exist.
        json.JSONDecodeError: If the file is not a valid JSON.
    """
    
    status = input("What status would you like to filter by?: \n")
    
    with open('tasks-database.json', 'r') as f:
        data = json.load(f)
        for task_id, task_data in data["tasks"].items():
            if task_data["status"] == status:
                print(f"Task ID: {task_id}")
                print(f"Description: {task_data['description']}")
                print(f"Status: {task_data['status']}")
                print(f"Created at: {task_data['created_at']}")
                print(f"Updated at: {task_data['updated_at']}")
                print("\n")

# Main function
def main():
    """
    Main function to handle user input and perform corresponding task operations.
    The function prompts the user for input and executes the appropriate task 
    management function based on the input command. The supported commands are:
    - "add": Adds a new task.
    - "test": Adds a test task.
    - "update": Updates an existing task.
    - "delete": Deletes a specific task.
    - "deleteall": Deletes all tasks.
    - "list": Lists all tasks.
    - "show": Shows details of a specific task.
    - "filter": Filters tasks based on certain criteria.
    """
    
    user_input = get_user_input()
    if user_input == "add":
        add_task()
    elif user_input == "test":
        add_test_task()
    elif user_input == "update":
        update_task()
    elif user_input == "delete":
        delete_task()
    elif user_input == "deleteall":
        delete_all_tasks()
    elif user_input == "list":
        list_tasks()
    elif user_input == "show":
        show_task()
    elif user_input == "filter":
        filter_tasks()

if __name__ == "__main__":
    database_creation()
    main()
