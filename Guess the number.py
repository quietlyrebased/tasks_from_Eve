import random

in_progress = True

while in_progress:
    number = random.randint(1, 100)
    attempts = 0

    print("Я загадал число от 1 до 100. Попробуй угадать!")

    while True:
        hunch = int(input("Твоя догадка: "))
        attempts += 1

        if hunch < number:
            print("Слишком мало!")
        elif hunch > number:
            print("Слишком много!")
        else:
            print(f"Верно! Ты угадал за {attempts} попыток.")
            break

    answer = input("Хочешь сыграть ещё раз?\nНапиши 'да' или 'нет': ").strip().lower()
    if answer != "да":
        in_progress = False