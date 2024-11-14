from datetime import datetime

class Task:
    def __init__(self, title, description, deadline):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        status = "Виконано" if self.completed else "Не виконано"
        return f"Назва: {self.title}\nОпис: {self.description}\nДедлайн: {self.deadline}\nСтан: {status}\n"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, deadline):
        task = Task(title, description, deadline)
        self.tasks.append(task)
        print(f"Завдання '{title}' додано.")

    def remove_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                print(f"Завдання '{title}' видалено.")
                return
        print(f"Завдання '{title}' не знайдено.")

    def mark_task_completed(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_as_completed()
                print(f"Завдання '{title}' відмічено як виконане.")
                return
        print(f"Завдання '{title}' не знайдено.")

    def show_tasks(self):
        if not self.tasks:
            print("Список завдань порожній.")
        else:
            for task in self.tasks:
                print(task)



manager = TaskManager()


manager.add_task("Підготувати звіт", "Підготувати звіт за місяць", "2024-11-30")
manager.add_task("Відвідати лікаря", "Плановий візит до лікаря", "2024-11-20")


print("\nСписок завдань:")
manager.show_tasks()


manager.mark_task_completed("Підготувати звіт")


print("\nОновлений список завдань:")
manager.show_tasks()


manager.remove_task("Відвідати лікаря")


print("\nФінальний список завдань:")
manager.show_tasks()
