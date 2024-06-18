def show_menu():
    print("\nTO-DO APP")
    print("1. Add a task")
    print("2. View the tasks")
    print("3. Remove a task")
    print("4. EXIT")

def add_task(tasks_list, task):
    if not task.strip():
        print("Cannot add an empty task.")
    elif task in tasks_list:
        print(f"Task '{task}' already exists in the list.")
    else:
        tasks_list.append(task)
        print(f"Task '{task}' added.")

def remove_task(tasks_list):
    if tasks_list:
        display_tasks(tasks_list)
        try:
            task_number = int(input("Enter the task number to remove: "))
            if 1 <= task_number <= len(tasks_list):
                removed_task = tasks_list.pop(task_number - 1)
                print(f"Task '{removed_task}' removed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a valid task number.")
    else:
        print("The to-do list is empty.")

def display_tasks(tasks_list):
    if tasks_list:
        print("\nTo-do list:")
        for idx, task in enumerate(tasks_list, 1):
            print(f"{idx}. {task}")
    else:
        print("The to-do list is empty.")

def switch_case(option, tasks_list):
    if option == '1':
        task = input("Enter the task to add: ")
        add_task(tasks_list, task)
    elif option == '2':
        display_tasks(tasks_list)
    elif option == '3':
        remove_task(tasks_list)
    elif option == '4':
        print("Exiting the application.")
        return False
    else:
        print("Invalid option, please try again.")
    return True

def main():
    tasks = ["reading", "writing", "playing"]
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if not switch_case(choice, tasks):
            break
    print("Thank you for using the to-do app!")

if __name__ == "__main__":
    main()