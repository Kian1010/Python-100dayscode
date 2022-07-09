from art import logo
import random


def check_guess(num_entered, correct_num, life):
    """
    Checks the input and returns a value based on if the guess was correct or not
    """
    if num_entered > correct_num:
        print("Too high.")
        return life-1
    elif num_entered < correct_num:
        print("Too low.")
        return life-1
    else:
        print(f"You got it! The answer was {correct_num}")
        return life-life


def check_life(life):
    print(f"You have {life} attempts remaining to guess the number.")


def start_game():
    print(logo)
    print("Welcome to the number guessing gameZ!")
    print("I'm thinking of a number between 1 and 100.")
    random_num = random.randint(1, 100)
    print(f"pssst, the answer is {random_num}")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty == "easy":
        player_life = 10
    else:
        player_life = 5

    check_life(player_life)
    guessed_number = 1
    while player_life != 0:
        guessed_number = int(input("Make a guess: "))
        player_life = check_guess(guessed_number, random_num, player_life)
        if player_life > 0:
            print("Guess again.")
            check_life(player_life)

    if guessed_number != random_num:
        print(f"You've run out of guesses, you lose")


start_game()
