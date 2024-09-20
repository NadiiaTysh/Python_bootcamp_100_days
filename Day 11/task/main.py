import art
import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(numbers):
    sum_of_numbers = sum(numbers)
    if len(numbers) == 2 and sum_of_numbers == 21:
        sum_of_numbers = 0
    elif sum_of_numbers > 21 and 11 in numbers:
        numbers.remove(11)
        numbers.append(1)
        sum_of_numbers = sum(numbers)
    return sum_of_numbers

def set_game_ended(user_scores, computer_scores):
    result = True
    if user_scores == 0:
        print("Blackjack. You Win")
    elif computer_scores == 0:
        print("Blackjack. Computer Wins")
    elif user_scores > 21:
        print("You Lose")
    elif computer_scores > 21:
        print("You Win")
    else:
        result = False
    return result

def compare_winner(user_scores, computer_scores):
    if user_scores > 21:
        print("You Lose")
    elif computer_scores > 21:
        print("You Win")
    elif computer_scores < user_scores <= 21:
        print(f"You Win with score {user_scores}")
    elif user_scores < computer_scores <= 21:
        print(f"Computer Wins with score {computer_scores}")
    elif user_scores == computer_scores:
        print(f"Draw with score {user_scores}")

def play_game():
    print(art.logo)
    user_cards = []
    computer_cards = []
    game_ended = False
    more_card = 'n'

    for time in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_ended:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score is {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        game_ended = set_game_ended(user_score, computer_score)
        is_winner_defined = True if game_ended else False

        while user_score < 21 and not user_score == 0 and not computer_score == 0:
            more_card = input("Do you want to draw another card? 'y' or 'n': ").lower()

            if more_card == 'n':
                game_ended = True
                break
            elif more_card == 'y':
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)
                print(f"Your cards: {user_cards}, current score is {user_score}")

        while calculate_score(computer_cards) < 17 and not user_score == 0 and not computer_score == 0:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)
            print(f"Computer's score is {computer_score}")
        else:
            game_ended = True

        if not is_winner_defined:
            compare_winner(user_score, computer_score)

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    print("\n" * 30)
    play_game()

# in_game = True
# found_winner = False
# while in_game:
#     more_card = "n"
#     user_score = calculate_score(user_cards)
#     computer_score = calculate_score(computer_cards)
#     print(f"Your score is {user_score}")
#     print(f"Computer's score is {computer_score}")
#     if user_score == 0:
#         print("Blackjack. You Win")
#         found_winner = True
#     elif computer_score == 0:
#         print("Blackjack. Computer Wins")
#         found_winner = True
#     elif user_score > 21:
#         print("You Lose")
#         found_winner = True
#     elif computer_score > 21:
#         print("You Win")
#         found_winner = True
#     elif user_score < 21:
#         more_card = input("Do you want to draw another card? 'y' or 'n': ").lower()
#
#     if more_card == 'n':
#         in_game = False
#         if computer_score < user_score <= 21 and not found_winner:
#             print(f"You Win with score {user_score}")
#             found_winner = True
#         elif user_score < computer_score and not found_winner:
#             print(f"Computer Wins with score {computer_score}")
#             found_winner = True
#         elif user_score == computer_score and not found_winner:
#             print(f"Draw with score {user_score}")
#             found_winner = True
#     elif more_card == 'y':
#         found_winner = False
#         user_cards.append(deal_card(cards))
#     else:
#         more_card = input("Please select 'y' or 'n'? ").lower()
