import art, os

print(art.logo)
all_bids = {}

more_bidders = True
while more_bidders:

    name = input('What is your name? ')
    bid = int(input('What\'s your bid? $'))
    if name not in all_bids:
        all_bids[name] = bid
    else:
        print('Invalid Bid: Duplicate Names')
    result = input('Are there any other bidders? Type \'yes\' or \'no\'.\n').lower()
    if result in  ['n', 'no']:
        more_bidders = False
    os.system('cls')

highest_bid = 0
highest_bidder = ''
for bidder in all_bids:
    if highest_bid < all_bids[bidder]:
        highest_bid = all_bids[bidder]
        highest_bidder = bidder
print(f'The winner is {highest_bidder} with a bid of ${highest_bid}.')