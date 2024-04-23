inventory = {}

def add_item():
    item_name = input("Введите название предмета: ")
    item_description = input("Введите описание предмета: ")
    inventory[item_name] = item_description
    print("Предмет успешно добавлен в инвентарь!")

def remove_item():
    item_name = input("Введите название предмета для удаления: ")
    if item_name in inventory:
        del inventory[item_name]
        print("Предмет успешно удален из инвентаря!")
    else:
        print("Предмет с таким названием не найден в инвентаре.")

def view_inventory():
    if inventory:
        print("Инвентарь:")
        for item_name, item_description in inventory.items():
            print(f"{item_name}: {item_description}")
    else:
        print("Инвентарь пуст.")

while True:
    print("\nМеню:")
    print("1. Добавить предмет в инвентарь")
    print("2. Удалить предмет из инвентаря")
    print("3. Просмотреть инвентарь")
    print("4. Выйти")

    choice = input("Выберите действие: ")

    if choice == '1':
        add_item()
    elif choice == '2':
        remove_item()
    elif choice == '3':
        view_inventory()
    elif choice == '4':
        break
    else:
        print("Неверный выбор. Пожалуйста, выберите снова.")
9