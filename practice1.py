import random


def guessing_game(number, name):
    print('You\'ll get 10 Guesses! Less go')
    for i in range(1, 11):
        guess_number = int(input(f'{name}, Enter Your Guess: '))
        if guess_number == number:
            print(f'{name}, Your Guess was correct')
            break
        elif guess_number > number:
            print(f'Too High! Guess remaining: {10-i}')

        elif guess_number < number:
            print(f'Too Low! Guess remaining: {10-i}')

        if i == 10:
            print('Game Over! Try Again')


def main():
    number = random.randint(0, 100)
    name = input('Enter your name: ')
    print(f'Hello, {name}')
    guessing_game(number, name)


if __name__ == '__main__':
    main()
