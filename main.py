MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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
    },
}

resources = {
    "water": {
        "amount": 300,
        "unit": "ml"
    },
    "milk": {
        "amount": 200,
        "unit": "ml",
    },
    "coffee": {
        "amount": 100,
        "unit": "g",
    },
    "money": {
        "amount": 0,
        "unit": "USD",
    },
}

app_status = "run"


def coin_handler(menu_item):
    total_cost = MENU[menu_item]["cost"]
    print(f"Please insert coins. The total cost is: ${total_cost:.2f}")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total_input = round(quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01, 2)
    if total_input >= total_cost:
        print(f"Here is ${(total_input - total_cost):.2f} in change.")
        return True
    else:
        print("Insufficient funds, returning coins.")
        return False


def coffee_ui(input_command):
    global app_status
    if input_command == "end":
        app_status = "end"
    elif input_command == "latte" or input_command == "cappuccino" or input_command == "espresso":
        if (MENU[input_command]["ingredients"]["water"] <= resources["water"]['amount']) and (
                MENU[input_command]["ingredients"]["coffee"] <= resources["coffee"]['amount']) and (
                MENU[input_command]["ingredients"]["milk"] <= resources["milk"]['amount']):
            if coin_handler(input_command):
                resources["water"]['amount'] -= MENU[input_command]["ingredients"]["water"]
                resources["coffee"]['amount'] -= MENU[input_command]["ingredients"]["coffee"]
                resources["milk"]['amount'] -= MENU[input_command]["ingredients"]["milk"]
                resources["money"]['amount'] += MENU[input_command]["cost"]
                print(f"Enjoy your {input_command}, enjoy!")
        else:
            print("Insufficient resources.")
    elif input_command == "report":
        for item in resources:
            print(f"{item}: {resources[item]['amount']}{resources[item]['unit']}")
        app_status = "restart"
    else:
        print("Please use a proper command!")


while True:

    coffee_ui(input("What would you like? (espresso/latte/cappuccino): "))
    if app_status == "end":
        break

