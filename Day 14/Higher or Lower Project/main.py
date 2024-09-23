import random
import art
import game_data

# Generate random data 1 and data 2
def get_formatted_record(record):
    return f"{record.get('name')}, a {record.get('description')}, from {record.get('country')}."

def print_info(x, y):
    # Write Compare A:
    print(f"Compare A: {get_formatted_record(x)}")
    # Write VS image
    print(art.vs)
    # Write Against B:
    print(f"Against B: {get_formatted_record(y)}")

a = random.choice(game_data.data)
b = random.choice(game_data.data)
continue_game = True
score = 0

# Write logo image
print(art.logo)

while continue_game:
    print_info(a, b)

    # Get user input "Who has more followers? Type 'A' or 'B': "
    choice = input("Who has more followers? Type 'A' or 'B': ").upper()

    # Compare and print
    if ((choice != 'A' and choice != 'B')
            or (a.get('follower_count') < b.get('follower_count') and choice == 'A')
            or (a.get('follower_count') > b.get('follower_count') and choice == 'B')):
        continue_game = False
    else:
        score += 1

    # Reassign B to A and generate new B
    a = b
    b = random.choice(game_data.data)

    # Add You're right! Current score: n or Sorry, that's wrong. Final score: n
    if continue_game:
        print(f"Add You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
