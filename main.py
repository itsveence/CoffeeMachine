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


def coffee_machine():
    money = 0.0
    # Asks user what they want
    options = ["espresso", "latte", "cappuccino", "off", "report"]

    is_on = True
    while is_on:

        # Process coins and add to storage
        def process_coin():
            coins = [0, 0, 0, 0]
            coin_name = ["quarters", "dimes", "nickles", "pennies"]
            print("Please insert coins.")
            index = 0
            while index <= (len(coins) - 1):
                coins[index] = input(f"How many {coin_name[index]}: ")
                if coins[index].isnumeric():
                    coins[index] = int(coins[index])
                    index += 1
                else:
                    print("Please input an integer")

            return coins[0] * 0.25 + coins[1] * 0.1 + coins[2] * 0.05 + coins[3] * 0.01

        entry = input("What would you like? (espresso/latte/cappuccino): ")
        if entry.lower() not in options:
            print("Invalid entry. Try again")
            continue

        # Turns off program
        if entry.lower() == 'off':
            is_on = False

        # Prints out report
        elif entry.lower() == 'report':
            print(f"Water: {resources['water']}ml\n"
                  f"Milk : {resources['milk']}ml\n"
                  f"Coffee: {resources['coffee']}g\n"
                  f"Money: ${money}")
            continue

        # Checks if resources are sufficient
        else:
            is_ingredient_enough = True
            for ingredient in MENU[entry.lower()]['ingredients']:
                if resources[ingredient] < MENU[entry.lower()]['ingredients'][ingredient]:
                    print(f"Sorry there is not enough {ingredient}.")
                    is_ingredient_enough = False
                if not is_ingredient_enough:
                    continue
            avail_fund = process_coin()

            # Check if transaction is successful
            if avail_fund < MENU[entry.lower()]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            else:
                money += MENU[entry.lower()]["cost"]
                for i in MENU[entry.lower()]['ingredients']:
                    resources[i] -= MENU[entry.lower()]['ingredients'][i]
                if avail_fund > MENU[entry.lower()]["cost"]:
                    change = avail_fund - MENU[entry.lower()]["cost"]
                    print(f"Here is ${round(change, 2)} dollars in change")
                    print(f"Here is your {entry.lower()}. Enjoy")


coffee_machine()
