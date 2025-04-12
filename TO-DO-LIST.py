tasks = []

while True:
    print("\nTO-DO LIST MENU")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Complete")
    print("4. Delete Task")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    # Add Task
    if choice == "1":
        task = input("Enter task description: ")
        tasks.append({"task": task, "done": False})
        print("Task added successfully!")
    
    # View Tasks
    elif choice == "2":
        if not tasks:
            print("Your list is empty!")
        else:
            print("\nYOUR TASKS:")
            for i in range(len(tasks)):
                status = "[DONE]" if tasks[i]["done"] else "[PENDING]"
                print(f"{i+1}. {status} {tasks[i]['task']}")
    
    # Mark Complete
    elif choice == "3":
        if not tasks:
            print("No tasks to mark complete!")
            continue
            
        print("\nYOUR TASKS:")
        for i in range(len(tasks)):
            status = "[DONE]" if tasks[i]["done"] else "[PENDING]"
            print(f"{i+1}. {status} {tasks[i]['task']}")
                
        try:
            task_num = int(input("Enter task number to mark complete: "))
            if 1 <= task_num <= len(tasks):
                if tasks[task_num-1]["done"]:
                    print("Task is already complete!")
                else:
                    tasks[task_num-1]["done"] = True
                    print("Task marked complete!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a number!")
    
    # Delete Task
    elif choice == "4":
        if not tasks:
            print("No tasks to delete!")
            continue
            
        print("\nYOUR TASKS:")
        for i in range(len(tasks)):
            status = "[DONE]" if tasks[i]["done"] else "[PENDING]"
            print(f"{i+1}. {status} {tasks[i]['task']}")
                
        try:
            task_num = int(input("Enter task number to delete: "))
            if 1 <= task_num <= len(tasks):
                deleted_task = tasks.pop(task_num-1)
                print(f"Deleted: {deleted_task['task']}")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a number!")
    
    # Exit
    elif choice == "5":
        print("Goodbye!")
        break
    
    # Invalid Choice
    else:
        print("Invalid choice! Please enter 1-5.")