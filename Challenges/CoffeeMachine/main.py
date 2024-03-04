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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report():
    """Run report for current resources and profit."""
    print("Water: {water}ml".format(**resources))
    print("Milk: {milk}ml".format(**resources))
    print("Coffee: {coffee}g".format(**resources))
    print(f"Money: ${profit:.2f}")


def coin_count(drink):
    """Gets coin count and determines if enough. With change function."""
    drink_cost = drink["cost"]
    print(f"The cost of the drink is ${drink_cost:.2f}")
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    total = quarters * .25 + dimes * .1 + nickels * .05 + pennies * .01
    if drink_cost > total:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    else:
        global profit
        profit += drink_cost
        print("Enjoy your drink!")
        if drink_cost != total:
            change = total - drink_cost
            print(f"Your change is : ${change:.2f}")
        return True


def resource_count(ingredients):
    """Compares user drink to resources and determines if enough."""
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry! There is not enough {item}.")
            return False
        else:
            return True


def resource_drain(ingredients):
    """Reduce the amount of resources."""
    for item in ingredients:
        resources[item] -= ingredients[item]


power = True

while power is True:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice == "off":
        power = False
        print("Power off")
    elif user_choice == "report":
        report()
    else:
        choice = MENU[user_choice]["ingredients"]
        cost = MENU[user_choice]
        is_enough_resources = resource_count(choice)
        if is_enough_resources is True:
            drink_bought = coin_count(cost)
            if drink_bought is True:
                resource_drain(choice)
