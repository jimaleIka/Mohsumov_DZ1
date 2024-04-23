import random
maxScore = [0]
name = input('Введите свое имя: ')
print("\nПравила игры:")
print(" ПК загадает 4-значное число, вам нужно угадать хотя бы одно. Если угодали получаете 10 очков. В случае неудачи вы поетряете одну из трех жизней!  В любой момент можно выйти игры нажав на кнопку 'Е' ")
print("Удачной игры вам!!!!")
def game():
    score = 0
    lives = 3
    while lives >= 1:
        randNum = str(random.randint(1000, 9999))
        numInput = input("Введите число от 0 до 9: ")
        if numInput == 'e':
            print(f'Ваш рекорд {max(maxScore)}')
            break
        elif randNum.count(str(numInput)) >= 1:
            score += 10
            print(f"Ваш счет: {score}")
            maxScore.append(score)
        elif int(numInput) > 9:
            print("Число превышает диапазон, введите другое")
            break
        elif lives != 1:
            lives -= 1
            print('У вас осталось ', lives, ' жизней')
        else:
            print(f'{name}, Вы проиграли. Ваши очки {score}. Ваш рекорд {max(maxScore)}')
            break
while True:
    game()
    isOver = input('Вы хотите продолжить игру? ')
    if isOver.lower() != 'да':
        break