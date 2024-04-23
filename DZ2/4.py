tasks = {
    "Бэклог": [],
    "В работе": [],
    "Выполнено": []
}


def show_tasks():
    for column, tasks_list in tasks.items():
        print(f"{column}:")
        for i, task in enumerate(tasks_list, 1):
            print(f"{i}. {task}")
        print()


def add_task():
    task = input("Введите новую задачу: ")
    tasks["Бэклог"].append(task)


def move_task():
    show_tasks()
    from_column = input("Из какой колонки переместить задачу (Бэклог, В работе, Выполнено): ")
    to_column = input("В какую колонку переместить задачу (Бэклог, В работе, Выполнено): ")

    if from_column in tasks and to_column in tasks:
        task_index = int(input("Введите номер задачи для перемещения: ")) - 1
        task = tasks[from_column].pop(task_index)
        tasks[to_column].append(task)
    else:
        print("Некорректные названия колонок.")


def remove_task():
    show_tasks()
    column = input("Из какой колонки удалить задачу (Бэклог, В работе, Выполнено): ")

    if column in tasks:
        task_index = int(input("Введите номер задачи для удаления: ")) - 1
        del tasks[column][task_index]
    else:
        print("Некорректное название колонки.")


while True:
    print("Меню:")
    print("1. Показать задачи")
    print("2. Добавить задачу")
    print("3. Переместить задачу")
    print("4. Удалить задачу")
    print("5. Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        move_task()
    elif choice == "4":
        remove_task()
    elif choice == "5":
        break
    else:
        print("Некорректный выбор. Попробуйте снова.")
