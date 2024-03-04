import random

computer_number = random.randint(1, 100)

while True:
    player = input("Guess the number (1-100): ")

    if not player.isdigit():
        print("Invalid input.Try again...")
        continue

    player_number = int(player)

    if player_number == computer_number:
        print("You guessed it!")
        break
    elif player_number < computer_number:
        print("Too low!")
    elif player_number > computer_number:
        print("Too high!")
