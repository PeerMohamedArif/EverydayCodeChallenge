logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________| 
"""

print(logo)
def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,

}

def calculator():
    Continue = True
    print("These are the operations available")
    for symbol in operations:
        print(symbol)
    num1= float(input("Give First Number"))
    while Continue:
        op= input("Pick an Operation")
        num2= float(input("Give Next Number"))
        calopr= operations[op]
        answer= calopr(num1,num2)
        print(f"\n\n{num1} {op} {num2} = {answer}")


        if input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation \n\n") == "y":
            num1 = answer
        else:
            Continue = False
            if input("do you want to quit the calculator type 'y' for yes else  'n' for no " )== 'n':

                calculator()
            else:
                return print(f"\n\nThe final answer is = {answer}")


calculator()
