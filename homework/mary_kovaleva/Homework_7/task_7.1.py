from random import randint

num = randint(1, 101)
guess = int(input('Введите целое число от 1 до 100: '))

while guess != num:
    if guess > num:
        print('Ваше число больше загаданного')
    elif guess < num:
        print('Ваше число меньше загаданного')
    guess = int(input('Попробуйте снова: '))

print('Поздравляю! Вы угадали!')
