from art import logo

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
    "money": 0,
}


def print_report():
    """ Print a report"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']} ")


def check_resources_sufficient(resources_coffee, prompt_user):
    """ Checks if the resources is sufficient to make the order"""
    water = MENU[prompt_user]["ingredients"]["water"]
    coffee = MENU[prompt_user]["ingredients"]["coffee"]
    water_remains = resources_coffee["water"] - water
    coffee_remains = resources_coffee["coffee"] - coffee
    milk_remains = 0
    if prompt_user == "latte" or prompt_user == "cappuccino":
        milk = MENU[prompt_user]["ingredients"]["milk"]
        milk_remains = resources_coffee["milk"] - milk
    if water_remains < 0:
        print("Sorry there is not enough water.")
    if coffee_remains < 0:
        print("Sorry there is not enough coffee.")
    if milk_remains < 0:
        print("Sorry there is not enough milk.")
    if water_remains >= 0 and coffee_remains >= 0 and milk_remains >= 0:
        return True
    else:
        return False


def process_coins(user_prompt):
    """ Process coins and return changes if the user entered money
    that is higher than the order price"""
    quarter = int(input("How many quarter do you have? :"))
    dimes = int(input("How many dimes do you have? :"))
    nickles = int(input("How many nickles do you have? :"))
    pennies = int(input("How many pennies do you have? :"))
    user_total = quarter * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    order_price = MENU[user_prompt]["cost"]
    if user_total >= order_price:
        changes = user_total - order_price
        print(f"I am processing now you coffee, here is the changes: ${changes}")
        resources['money'] += MENU[user_prompt]["cost"]
        return True
    else:
        print("You haven't enough money, money refunded ...")
        return False


def deduct_resources(user_prompt):
    """ calculate the resources that remains after every order """
    resources['water'] -= MENU[user_prompt]["ingredients"]["water"]
    resources['coffee'] -= MENU[user_prompt]["ingredients"]["coffee"]
    if user_prompt == "latte" or user_prompt == "cappuccino":
        resources['milk'] -= MENU[user_prompt]["ingredients"]["milk"]
    print(f"Here is your {user_prompt}. Enjoy!")


print(logo)
turn_on = True
while turn_on:
    prompt = input("What would you like? (espresso/latte/cappuccino):")
    if prompt != "report" and prompt != "off":
        if check_resources_sufficient(resources, prompt):
            if process_coins(prompt):
                deduct_resources(prompt)
    elif prompt == 'report':
        print_report()
    elif prompt == 'off':
        turn_on = False
