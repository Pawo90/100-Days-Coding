from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create object
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

machine_state = True

while machine_state:

    choice = input(f'What would you like? ({menu.get_items()}): ')
    drink = menu.find_drink(choice)

    if choice == 'off':
        machine_state = False
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
