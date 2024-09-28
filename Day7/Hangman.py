from hangmanart import hangmanpics
from wordlist import word_list,logo
import random

print(logo)
hangmanpics.reverse()
print(hangmanpics[0], "\n \n \n")
lives=6
print("TOTAL LIVES IS 6")
random1=random.choice(word_list)
#print(random1)
actual_word_list = list(random1)

blank_dash=""
for position in range(len(actual_word_list)):
    blank_dash += "_ "

print("FOR BELOW BLANKS FIND THE WORD BY guessed_wordING LETTERS ONE BY ONE OR GET HANGED")
print("\n\n\n\n",blank_dash,"\n\n\n\n")

game_over= False

correct_letters=[]
while not (game_over):
    guessed_word = input("guessed_word A LETTER : ").lower()
    display=""
    for letter in actual_word_list:
        if letter == guessed_word:
            display+= letter+ " "
            correct_letters.append(guessed_word)
        elif(letter in correct_letters):
            display+= letter
        else:
            display+="_ "

    print("\n\n\n",display,"\n\n\n")

    if guessed_word not in actual_word_list:
        if(lives!=0):
            print(f"The letter \"{guessed_word}\" is not in the word. You lose a life.")
            lives-=1

    print("Remaining Lives ==",lives,"\n\n")
    print(hangmanpics[lives])

    if "_" not in display:
        game_over=True
        print(" ************************  Congratulations, You WIN  **************************")
        print("You guessed_worded the WORD")
    elif lives==0:
        print("*************************  Game Over, You LOSE  **********************************")
        game_over=True
        print("The WORD is",random1)

