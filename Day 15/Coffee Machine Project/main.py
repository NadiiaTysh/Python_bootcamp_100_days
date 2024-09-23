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

machine_is_on = True
resources_are_sufficient = True
try_again = True
transaction_is_successful = False
money_collected = 0
payed_money = 0
beverage_selected = ""

def ask_for_beverage():
    """collects user input and returns either espresso, latte, cappuccino, off, report or invalid"""
    selected = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if selected in ["espresso", "latte", "cappuccino", "off", "report"]:
        return selected
    return "invalid"

def set_machine_off():
    """machine_is_on sets to False"""
    return False

def show_report(resource, money):
    """takes current resources and money and prints a report"""
    print(f"Water: {resource['water']}ml\n"
          f"Milk: {resource['milk']}ml\n"
          f"Coffee: {resource['coffee']}g\n"
          f"Money: {money}")

def check_resources_are_sufficient(available, requested):
    """takes available and requested resources and returns True if they are sufficient and False if not"""
    is_sufficient = True
    if requested.get("water") > available.get("water"):
        print("Sorry there is not enough water.”")
        is_sufficient = False
    if (not requested.get("milk") is None) and (requested.get("milk") > available.get("milk")):
        print("Sorry there is not enough milk.”")
        is_sufficient = False
    if requested.get("coffee") > available.get("coffee"):
        print("Sorry there is not enough coffee.”")
        is_sufficient = False
    return is_sufficient

def process_coins(quarters, dimes, nickles, pennies):
    """takes number of quarters, dimes, nickles, pennies and returns total amount of $"""
    quarter_value = 0.25
    dime_value = 0.10
    nickle_value = 0.05
    pennie_value = 0.01
    return quarters*quarter_value + dimes*dime_value + nickles*nickle_value + pennies*pennie_value

def deduct_ingredients(available, requested):
    """takes available and requested resources, deducts and returns what left"""
    available["water"] -= requested.get("water")
    available["coffee"] -= requested.get("coffee")
    if not requested.get("milk") is None:
        available["milk"] -= requested.get("milk")
    return available

while machine_is_on and try_again:
    # TODO 1 Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    beverage_selected = ask_for_beverage()

    # TODO 2 Turn off the Coffee Machine by entering “off” to the prompt
    if beverage_selected == "off":
        machine_is_on = set_machine_off()
    # TODO 3 Print report.
    elif beverage_selected == "report":
        show_report(resources, money_collected)
    elif beverage_selected == "invalid":
        continue
    else:
        try_again = False
else:
    if machine_is_on and resources_are_sufficient:
        # TODO 4 Check resources sufficient?
        resources_are_sufficient = check_resources_are_sufficient(resources, MENU.get(beverage_selected).get("ingredients"))

        # TODO 5 Process coins.
        print("Please insert coins.")
        quarters_inserted = int(input("how many quarters?:" ))
        dimes_inserted = int(input("how many dimes?: "))
        nickles_inserted = int(input("how many nickles?: "))
        pennies_inserted = int(input("how many pennies?: "))
        payed_money = process_coins(quarters_inserted, dimes_inserted, nickles_inserted, pennies_inserted)

        # TODO 6 Check transaction successful?
        beverage_selected_cost = MENU.get(beverage_selected).get("cost")
        if payed_money >= beverage_selected_cost:
            money_collected += payed_money
            if payed_money > beverage_selected_cost:
                print(f"Here is ${payed_money-beverage_selected_cost} dollars in change.")
            transaction_is_successful = True
        else:
            print(f"Sorry that's not enough money - ${payed_money}. Money refunded.")

        # TODO 7 Make Coffee
        if transaction_is_successful:
            resources = deduct_ingredients(resources, MENU.get(beverage_selected).get("ingredients"))
            print(f"Here is your {beverage_selected}. Enjoy!")
