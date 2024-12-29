import os
import json
import emoji

Data_Dir="Data"
Task_file=os.path.join(Data_Dir,"tasks.json")

if not os.path.exists(Data_Dir): #Making sure directory exists
    os.makedirs(Data_Dir)

tasks=[]

# Load tasks
def load_tasks():
    if os.path.exists(Task_file):
        with open(Task_file,"r") as file:
            return json.load(file)
    return []

# Saving tasks
def save_tasks():
    with open(Task_file,"w") as file:
        json.dump(tasks, file, indent=4)

# Create Backup
def backup_file():
    if os.path.exists(Task_file):
        backup_name=Task_file.replace(".json", "backup.json")
        os.rename(Task_file, backup_name)
        print(f"Backup created: {backup_name}")

# Clearing console
def clear_console():
    os.system('cls' if os.name== 'nt' else 'clear')

# Main Menu
def show_Menu():
    print("To-Do List Application")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")

# View Task
def view_task():
    if not tasks:
        print("No Tasks in the list.")
    else:
        print("Your Tasks:")
        for i, task in enumerate(tasks,1):
            status = emoji.emojize(":check_mark_button:") if task['completed'] else emoji.emojize(":white_large_square:")
            print(f"{i}.{status} {task['name']}")

# Add task
def add_task():
    task_name = input("Enter the task name: ").strip()
    if task_name:
        tasks.append({"name": task_name, "completed": False})
        print(f"Task '{task_name} added!")
    else:
        print("Task name cannot be empty.")

# Mark task as complete
def complete_task():
    view_task()
    try:
        task_num= int(input("Enter the task number to mark as complete: "))
        if 1<=task_num<=len(tasks):
            tasks[task_num-1]['completed'] = True
            print(f"Task '{tasks[task_num-1]['name']}' marked as complete!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Delete Task
def delete_task():
    view_task()
    try:
        task_num=int(input("Enter the task number to delete: "))
        if 1<=task_num<=len(tasks):
            removed_task= tasks.pop(task_num-1)
            print(f"Task '{removed_task['name']} deleted!")
        else:
            print("Invald task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    global tasks
    tasks=load_tasks()
    while True:
        clear_console
        show_Menu()
        try:
            choice=int(input("Choose an option: "))
            if choice==1:
                view_task()
            elif choice==2:
                add_task()
            elif choice==3:
                complete_task()
            elif choice==4:
                delete_task()
            elif choice==5:
                backup_file()
                save_tasks()
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please choose again.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ =="__main__":
    main()