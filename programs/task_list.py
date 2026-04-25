def task_list():
    print("\n--- Task List ---")
    tasks = []

    def show():
        if not tasks:
            print("No tasks yet.")
        else:
            for i, t in enumerate(tasks, 1):
                status = "✓" if t["done"] else "✗"
                print(f"{i}. {t['title']} [{status}]")

    while True:
        print("\n1. Add Task\n2. Complete Task\n3. Show Tasks\n4. Exit")
        choice = input("Choose: ")

        if choice == "1":
            title = input("Task title: ")
            tasks.append({"title": title, "done": False})

        elif choice == "2":
            show()
            idx = int(input("Task number: ")) - 1
            if 0 <= idx < len(tasks):
                tasks[idx]["done"] = True

        elif choice == "3":
            show()

        elif choice == "4":
            break
