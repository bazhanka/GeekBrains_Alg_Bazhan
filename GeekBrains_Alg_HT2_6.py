import random
num = random.randint(0,101)
count = 0
while count < 10:
    guess = int(input('Угадайте число от 0 до 100 '))
    if count == 9:
        print (f'Попытки истекли. Мы загадали число {num}')
        break
    elif guess == num:
        print (f"Верно! Мы загадали число {num}")
        break
    elif guess > num:
        count += 1
        print(f"Неверно! Загаданное число меньше вашего. Осталось попыток:{10-count}")
    elif guess < num:
        count += 1
        print (f"Неверно! Загаданное число больше вашего. Осталось попыток:{10-count}")