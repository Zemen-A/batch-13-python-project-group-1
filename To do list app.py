
def todo_list_app():
    tasks = []

    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Complete")
        print("Type 'exit' to quit.")

        choice = input("Select an option: ").strip().lower()
        
        if choice == "exit":
            break
        elif choice == "1":
            task = input("Enter the task: ")
            tasks.append({"task": task, "completed": False})
        elif choice == "2":
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task['task']} [{status}]")
        elif choice == "3":
            task_number = int(input("Enter the task number to delete: ")) - 1
            if 0 <= task_number < len(tasks):
                tasks.pop(task_number)
        elif choice == "4":
            task_number = int(input("Enter the task number to mark as complete: ")) - 1
            if 0 <= task_number < len(tasks):
                tasks[task_number]["completed"] = True

    # Summary
    completed_count = sum(task["completed"] for task in tasks)
    print(f"\nSummary: {completed_count} completed tasks, {len(tasks) - completed_count} pending tasks.")

todo_list_app()