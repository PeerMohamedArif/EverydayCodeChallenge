import random

logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
# print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    card = random.choice(cards)
    return card

def calculate_score(cards):
    total = sum(cards)

    if total == 21 and len(cards) == 2:
        return 0
    if 11 in cards and total > 21:
        cards.remove(11)
        cards.append(1)
    return total

def compare_scores(userscore, computerscore1):
    if userscore == computerscore1:
        return "DRAW"
    elif computerscore1 == 0:
        return "Computer has a blackjack You LOSE"
    elif userscore == 0:
        return "You have a BlackJack You WIN"
    elif userscore > 21:
        return "You Lose, You exceeded the limit"
    elif computerscore1 > 21:
        return "Computer exceeded the limit, You WIN"
    elif userscore > computerscore1:
        return "You WIN"
    else:
        return "Computer WIN, You LOSE"

# assign cards to user and computer
def playgame():
    usercards = []
    computercards = []
    computerscore = -1  # not 0 because 0 is blackjack in our game
    userscore = -1
    game_over = False
    for i in range(0, 2):
        usercards.append(deal_card())
        computercards.append(deal_card())
    while not game_over:
        userscore = calculate_score(usercards)
        computerscore = calculate_score(computercards)
        print(f"Your Cards: {usercards}. Your current score: {userscore}")
        print(f"The Computer's First card: {computercards[0]}")

        if userscore == 0 or computerscore == 0 or userscore > 21:
            game_over = True
        else:
            user_want_card = input("Type 'y' to get another card, if not type 'n': ")
            if user_want_card == 'y':
                usercards.append(deal_card())
            else:
                game_over = True

    while computerscore != 0 and computerscore < 17:
        computercards.append(deal_card())
        computerscore = calculate_score(computercards)

    print(f"Your final score is {21 if userscore == 0 else userscore} and your cards were {usercards}")
    print(f"Computer score is {21 if computerscore == 0 else computerscore} and Computer's cards were {computercards}")

    print(compare_scores(userscore, computerscore))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n':") == "y":
    print(logo)
    playgame()
