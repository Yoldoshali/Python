from ascii import image
print(image)
print("Welcome to the secret auction program")
game_over = False
bid_list = {}


def compare(bidders):
    biggest_bid = 0
    winner_name = ''
    for bidder in bidders:
        if bidders[bidder] > biggest_bid:
            biggest_bid = bidders[bidder]
            winner_name = bidder
    return f"Winner is {winner_name.capitalize()} with a bid of ${biggest_bid}"


while not game_over:
    name = input("What is your name?\n>>")
    bid = float(input("What is your bid?\n>>$"))
    bid_list[name] = bid
    other_bidder = input("Are there any other bidders?(yes/no)\n>>")
    if other_bidder == 'yes':
        game_over = False
        print('\n'*20)
    else:
        game_over = True
        print("\n"*50)
        print(compare(bid_list))
