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
    "water": [300, 'ml'],
    "milk": [200, 'ml'],
    "coffee": [100, 'g']
}


#   TODO: 1. Print report of all coffee machine resources
def report():
    for resurce in resources:
        print(f"{resurce}: {resources[resurce][0]} {resources[resurce][1]}")


#   TODO: 2. Update or check resources
def check_resources(resources, menu, choice, update):
    if not update:
        for ingradient in menu[choice]['ingredients']:
            if resources[ingradient][0] < menu[choice]['ingredients'][ingradient]:
                return f"Sorry there is not enough {ingradient}"
        return 'OK'
    else:
        for ingradient in menu[choice]['ingredients']:
            resources[ingradient][0] -= menu[choice]['ingredients'][ingradient]


#   TODO: 3. Process
def process_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


turn_off = False
while not turn_off :
    choice = input('What would you like? (espresso/latte/cappuccino): ')
    if choice == 'turn off':
        turn_off = True
    elif not choice == 'report':
        check_result = check_resources(resources, MENU, choice, False)
        if check_result == 'OK':
            coins = process_coins()
            print(coins)
            if coins < MENU[choice]['cost']:
                print("Sorry that's not enough money, Money refunded.")
            elif coins > MENU[choice]['cost']:
                change = round((coins - MENU[choice]['cost']), 2)
                print(f'''Here is ${change} in change\nHere is your {choice}. Enjoy!''')
                check_resources(resources, MENU, choice, True)
            else:
                print(f'Here is your {choice}. Enjoy!')
                check_resources(resources, MENU, choice, True)
        else:
            print(check_result)
    elif choice == 'report':
        report()


