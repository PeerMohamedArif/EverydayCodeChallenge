from higherorlowerdata import data
import random

logo = r"""
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
/ /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = r"""
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""
score = 0
game_over = False
def random_choice():
    A_value = random.choice(data)
    B_value = random.choice(data)
    return [A_value, B_value]
while not game_over:
    to_compare = random_choice()

    print(f"Compare A: {to_compare[0]['name']}, {to_compare[0]['description']}, from {to_compare[0]['country']}")
    print(f"\n\n{vs}\n\n")
    print(f"Against B: {to_compare[1]['name']}, {to_compare[1]['description']}, from {to_compare[1]['country']}")
    given_value = input("Who has more followers? Type 'A' or 'B': ").lower()

    def print_score_add():
        # Use the global score variable
        global score
        score += 1
        print(f"**************You are right, Current Score: {score}**************")

    def compare():
        global game_over  # Declare global at the start of the function
        if given_value == 'a':
            if to_compare[0]['follower_count'] > to_compare[1]['follower_count']:
                print_score_add()
            else:
                print(f"Sorry, that's wrong. Your final score: {score}")
                game_over = True
        elif given_value == 'b':
            if to_compare[1]['follower_count'] > to_compare[0]['follower_count']:
                print_score_add()
            else:
                print(f"Sorry, that's wrong. Your final score: {score}")
                game_over = True
        else:
            print("Invalid input, try again")

    compare()



