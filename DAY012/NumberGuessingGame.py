import random

EASY_LEVEL = 10
HARD_LEVEL = 5
logo = r'''
 _______  __   __  _______  _______  _______    _______  __   __  _______    __    _  __   __  __   __  _______  _______  ______      __     __     __  
|       ||  | |  ||       ||       ||       |  |       ||  | |  ||       |  |  |  | ||  | |  ||  |_|  ||  _    ||       ||    _ |    |  |   |  |   |  | 
|    ___||  | |  ||    ___||  _____||  _____|  |_     _||  |_|  ||    ___|  |   |_| ||  | |  ||       || |_|   ||    ___||   | ||    |  |   |  |   |  | 
|   | __ |  |_|  ||   |___ | |_____ | |_____     |   |  |       ||   |___   |       ||  |_|  ||       ||       ||   |___ |   |_||_   |  |   |  |   |  | 
|   ||  ||       ||    ___||_____  ||_____  |    |   |  |       ||    ___|  |  _    ||       ||       ||  _   | |    ___||    __  |  |__|   |__|   |__| 
|   |_| ||       ||   |___  _____| | _____| |    |   |  |   _   ||   |___   | | |   ||       || ||_|| || |_|   ||   |___ |   |  | |   __     __     __  
|_______||_______||_______||_______||_______|    |___|  |__| |__||_______|  |_|  |__||_______||_|   |_||_______||_______||___|  |_|  |__|   |__|   |__| 
'''
def game():
    def difficultylevel():
        difficulty= input("Choose a difficulty level. Type EASY or HARD").lower()
        if difficulty== 'easy':
            return EASY_LEVEL
        elif difficulty== 'hard':
            return HARD_LEVEL
        else:
            print("Invalid Input")
            difficultylevel()

    number_of_chances= difficultylevel()

    def choose_random_number():
        number= random.randint(1,100)
        return number
    def check_number(user_guess,actual_answer,chances):
        if user_guess>actual_answer:
            print("Too High")
            return chances-1
        if user_guess<actual_answer:
            print("Too Low")
            return chances-1
        else:
            print("You have found out the nuumber")
            print(f"the number was {actual_answer}")
            return chances

    print(logo)
    print("Welcome to The Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    answer= choose_random_number()
    guess=0
    while guess!= answer:
        print(f"You have {number_of_chances} remaining.")
        guess = int(input("Make a guess:"))
        number_of_chances=check_number(guess,answer,number_of_chances)
        if number_of_chances<=0:
            print("You have exhausted all your chances, You Lose")
            return
        elif guess!=answer:
            print("you can guess again")

game()
