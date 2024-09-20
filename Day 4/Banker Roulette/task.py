import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

index_of_friends = random.randint(0, len(friends) - 1)
print(f"One option pays: {friends[index_of_friends]}")

another_option_friend = random.choice(friends)
print(f"Another option pays friend: {another_option_friend}")
