from art import logo

print(logo)
max_bid = 0
max_bidder = ""
continue_bidding = True
bidders_and_bids = {}
while continue_bidding:
    # TODO-1: Ask the user for input
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    others = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    # TODO-2: Save data into dictionary {name: price}
    bidders_and_bids[name] = bid
    # TODO-3: Whether if new bids need to be added
    if others == 'no':
        continue_bidding = False
    print("\n" * 20)

# TODO-4: Compare bids in dictionary
for key in bidders_and_bids:
    if bidders_and_bids[key] > max_bid:
        max_bid = bidders_and_bids[key]
        max_bidder = key

print(f"The winner is {max_bidder} with a bid of ${max_bid}.")
