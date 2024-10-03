logo = r'''

                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________
                       .-------------.
                      /_______________
'''


bid_list = {}

def get_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for key in bidding_record:
        bid_amount= bidding_record[key]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=key
    print(f'\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n'
          f'*****************the winner and the highest bidder is {winner} with a bid of {highest_bid} ****************** ')


print(logo)




continue_bids = True
while continue_bids:
    name = input("What is your name?:")
    bid = int(input("How much are you bidding in dolllars: $"))

    bid_list[name]=bid

    should_continue = input("Is there anyone else who wants to bid? 'yes' or 'no'").lower()
    if should_continue=='no':
        continue_bids= False
        get_highest_bidder(bid_list)
    else:
        print("\n" * 75)






