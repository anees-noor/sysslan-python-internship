tasks = []

while True:
    print("\n===== DAILY TASK MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)

        with open("tasks.txt", "a") as file:
            file.write(task + "\n")

        print("Task saved successfully!")

    elif choice == "2":
        try:
            with open("tasks.txt", "r") as file:
                print("\nYour Daily Tasks:")

                for line in file:
                    print(line, end="")

        except FileNotFoundError:
            print("No tasks found.")

    elif choice == "3":
        print("Exiting Task Manager...")
        break

    else:
        print("Invalid choice!")