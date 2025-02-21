from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine= MoneyMachine()
coffeemaker= CoffeeMaker()
menu=Menu()
is_on=True
while is_on:
    options =menu.get_items()
    choice=input(f'What would you like?{options}')
    if choice=='off':
        is_on=False
    elif(choice=='report'):
        coffeemaker.report()
        money_machine.report()
    else:
        drink=menu.find_drink(choice)
        if coffeemaker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffeemaker.make_coffee(drink)







