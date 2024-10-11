# Simple To-Do List
todo_list = []

def view_tasks():
    if not todo_list:
        print("Your to-do list is empty!")
    else:
        print("Your to-do list:")
        for idx, task in enumerate(todo_list, start=1):
            print(f"{idx}. {task}")

def add_task():
    task = input("Enter a new task: ")
    todo_list.append(task)
    print(f"Task '{task}' added.")

def remove_task():
    view_tasks()
    if todo_list:
        task_num = int(input("Enter task number to remove: "))
        if 0 < task_num <= len(todo_list):
            removed = todo_list.pop(task_num - 1)
            print(f"Task '{removed}' removed.")
        else:
            print("Invalid task number.")

while True:
    print("\n1. View tasks\n2. Add task\n3. Remove task\n4. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        break
    else:
        print("Invalid option.")
