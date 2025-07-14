import random


def guess_the_number():
    """Игра 'Угадай число'."""
    secret_number = random.randint(1, 100)  # Загадываем число от 1 до 100
    attempts = 0

    print("Привет! Я загадал число от 1 до 100.")
    print("Попробуй его угадать!")

    while True:
        try:
            user_guess = int(input("Введите ваше предположение: "))
            attempts += 1

            if user_guess < secret_number:
                print("Мое число больше.")
            elif user_guess > secret_number:
                print("Мое число меньше.")
            else:
                print(f"Поздравляю! Вы угадали число {secret_number} за {attempts} попыток.")
                break
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число.")
        except Exception as e:
            print(f"Произошла непр234567едвиденная ошибка: {e}")


if __name__ == "__main__":
    guess_the_number()

