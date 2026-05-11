from src.task_manager import (
    add_task,
    complete_task,
    list_tasks,
    TaskNotFoundError
)

def main() -> None:
    while True:
        print("Task Tracker")
        print("1. Add task")
        print("2. List tasks")
        print("3. Complete task")
        print("4. Exit")

        choice = input("Choose an option: ")
        try:
            if choice == "1":
                title = input("Task title: ")
                add_task(title)
            elif choice == "2":
                list_tasks()
            elif choice == "3":
                task_index = int(input("task number: "))
                complete_task(task_index)
            elif choice == "4":
                print("Goodbye")
                break
            else:
                print("Invalid option") 
        except TaskNotFoundError as error:
            print(error)
        except ValueError:
            print("Please enter a valid number")

if __name__ == "__main__":
    main()