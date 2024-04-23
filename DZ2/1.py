import random

questions = []

def add_question():
    question = input("Введите новый вопрос: ")
    questions.append(question)
    print("Вопрос успешно добавлен!")

def edit_question():
    index = int(input("Введите индекс вопроса для редактирования: "))
    if 0 <= index < len(questions):
        new_question = input("Введите новую версию вопроса: ")
        questions[index] = new_question
        print("Вопрос успешно отредактирован!")
    else:
        print("Неверный индекс вопроса.")

def delete_question():
    index = int(input("Введите индекс вопроса для удаления: "))
    if 0 <= index < len(questions):
        del questions[index]
        print("Вопрос успешно удален!")
    else:
        print("Неверный индекс вопроса.")

def get_random_question():
    if questions:
        random_question = random.choice(questions)
        print("Случайный вопрос: ", random_question)
    else:
        print("Список вопросов пуст.")

while True:
    print("\nМеню:")
    print("1. Добавить вопрос")
    print("2. Редактировать вопрос")
    print("3. Удалить вопрос")
    print("4. Получить случайный вопрос")
    print("5. Выйти")

    choice = input("Выберите действие: ")

    if choice == '1':
        add_question()
    elif choice == '2':
        edit_question()
    elif choice == '3':
        delete_question()
    elif choice == '4':
        get_random_question()
    elif choice == '5':
        break
    else:
        print("Неверный выбор. Пожалуйста, выберите снова.")
