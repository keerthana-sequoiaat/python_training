def show_menu():
    print("\nTO-DO APP")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. EXIT")

def add_task(tasks_list):
    task = input("Enter the task to add: ").strip()
    if not task:
        print("Cannot add an empty task.")
        return
    category = select_category()
    priority = select_priority()
    if any(t['task'] == task for t in tasks_list):
        print(f"Task '{task}' already exists in the list.")
    else:
        tasks_list.append({'task': task, 'category': category, 'priority': priority})
        print(f"Task '{task}' added to the {category} {priority} priority list.")

def remove_task(tasks_list):
    if tasks_list:
        display_tasks(tasks_list)
        try:
            task_number = int(input("Enter the task number to remove: "))
            if 1 <= task_number <= len(tasks_list):
                removed_task = tasks_list.pop(task_number - 1)
                print(f"Task '{removed_task['task']}' removed.")
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
            print(f"{idx}. {task['task']} {task['category']},{task['priority']}")
    else:
        print("The to-do list is empty.")

def select_category():
    while True:
        category = input("Enter the category (personal/professional): ").strip().lower()
        if category in ['personal', 'professional']:
            return category
        else:
            print("Invalid category. Please enter 'personal' or 'professional'.")

def select_priority():
    while True:
        priority = input("Enter the priority (high/low):")
        if priority in ['high', 'low']:
            return priority
        else:
            print("Invalid priority. Please enter 'high' or 'low'.")
def create_summary_file(tasks_list):
    with open('summary.txt', 'w') as file:
        for task in tasks_list:
            file.write(f"{task['task']}, {task['category']}, {task['priority']}\n")
    print('Summary file has been created!')

def switch_case(option, tasks_list):
    if option == '1':
        add_task(tasks_list)
    elif option == '2':
        display_tasks(tasks_list)
    elif option == '3':
        remove_task(tasks_list)
    elif option == '4':
        print("Exiting the application.")
        create_summary_file(tasks_list)
        return False
    else:
        print("Invalid option")
    return True

def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if not switch_case(choice, tasks):
            break
    print("thank you")

if __name__ == "__main__":
    main()
