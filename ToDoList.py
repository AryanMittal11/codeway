class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task Added Successfully")

    def update_task(self, index, new_task):
        if 0 <= index < len(self.tasks):
            self.tasks[index] = new_task
            print("Task Update successfully")
        else:
            print("Invalid index, Please Try again!")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            print("Task Delete Successfully")
        else:
            print("Invalid Index, Please Try Again!")

    def display_task(self):
        if self.tasks:
            print("TO Do List: ")
            for i, task in enumerate(self.tasks):
                print(f"{i + 1}. {task}")
        else:
            print("Your To Do List is empty")


def main():
    todo_list = ToDoList()

    while True:
        print("Select an option:")
        print("1. Add task")
        print("2. Update task")
        print("3. Delete task")
        print("4. View To Do List")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter new task: ")
            todo_list.add_task(task)
        elif choice == "2":
            index = int(input("Enter index you want to update: ")) - 1
            new_task = input("Enter task: ")
            todo_list.update_task(index, new_task)
        elif choice == "3":
            index = int(input("Enter index you want to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == "4":
            todo_list.display_task()
        elif choice == "5":
            print("Exiting Program")
            break
        else:
            print("Invalid Choice, Please Try Again")


if __name__ == "__main__":
    main()
