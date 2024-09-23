import art
import random

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number_to_guess = random.randint(1, 100)
number_of_attempts = 5

difficulty = input("Choose difficulty. Type 'easy' or 'hard': ")
levels = {"easy": "easy", "hard": "hard"}
if difficulty == levels["easy"]:
    number_of_attempts = 10
elif not difficulty == levels["hard"]:
    difficulty = input("Choose correct difficulty. Type 'easy' or 'hard': ")

while number_of_attempts > 0:
    print(f"You have {number_of_attempts} attempts remaining to guess the number.")
    proposed_number = int(input("Make a guess: "))
    if proposed_number == number_to_guess:
        print(f"You got it! The answer was {number_to_guess}")
        break
    elif proposed_number < number_to_guess:
        print("Too low.")
    elif proposed_number > number_to_guess:
        print("Too high.")

    print("Guess again.")
    number_of_attempts -= 1
else:
    print("You've run out of guesses, you lose.")
