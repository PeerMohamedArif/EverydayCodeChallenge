import random


rock=  ("""
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """)
paper=("""
                     _______
                ---'    ____)____
                           ______)
                          _______)
                         _______)   
                ---.__________)
                """)
scissor=("""
                    _______
                ---'   ____)____
                          ______)
                       __________)
                      (____)
                ---.__(___)
                """)
choice_list=[rock,paper,scissor]
def rpscall():
    value=int(input("Give '0' for rock, '1' for paper,'2' for scissors "))
    while value not in [0, 1, 2]:
        print("invalid choice, Please give values within 0,1,2")
        rpscall()
        break
    def rps():
        random1=random.randint(0,2)
        if (random1 == 0):
            print(choice_list[0])
        elif (random1 == 1):

            print(choice_list[1])
        else:
            print(choice_list[2])
        return random1
    if (value== 0):
        print(choice_list[0])
        random2=rps()
        if (random2==0):
            print("its a Draw")
        elif(random2==1):
            print("paper beats rock, you lose")
        elif(random2==2):
            print("rock beats scissors, you win")
    elif(value==1):
        print(choice_list[1])
        random2=rps()
        if (random2==1):
            print("its a Draw")
        elif(random2==0):
            print("paper beats rock, you win")
        elif(random2==2):
            print("scissors beat paper, you lose")
    elif(value==2):
        print(choice_list[2])
        random2=rps()
        if (random2==2):
            print("its a Draw")
        elif(random2==0):
            print("rock beats scissors, you lose")
        elif(random2==1):
            print("scissors beat paper, you win")
rpscall()

