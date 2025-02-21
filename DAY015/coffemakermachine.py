MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]> resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
        return True
def transaction_success(paymentreceived,drink_cost):
    global profit
    if paymentreceived>=drink_cost:
        profit+=drink_cost
        change=round((paymentreceived-drink_cost),2)
        print(f'Here is your change :{change}')
        return True
    else:
        print("Sorry ,Not enough Money was provided, Money refunded")
        return False
def make_drink(drink_decision, drink_ingredients):
    for item in drink_ingredients:
        resources[item]-=drink_ingredients[item]
    print(f'Here is your {drink_decision} ☕ , Have a wonderful day ahead')
def process_coins():
    total=0
    print("Insert coins")
    total+= int(input("How many Quarters"))*0.25
    total+= int(input("How many Dimes"))*0.10
    total+= int(input("How many Nickels"))*0.05
    total+= int(input("How many Pennies"))*0.01
    return total
machine_on= True
profit=0
while machine_on :
    decision=input('What would you like? (espresso/latte/cappuccino):')
    if decision=='off':
        machine_on= False
    elif decision=='report':
        print(f"Water: {resources['water']}ml ")
        print(f"Milk: {resources['milk']}ml ")
        print(f"Coffee: {resources['coffee']}g ")
        print(f"Money: ${profit} ")
    else:
        drink=MENU[decision]
        if resources_sufficient(drink['ingredients']):
            payment=process_coins()
            if transaction_success(payment, drink['cost']):
                make_drink(decision,drink['ingredients'])
