def coffee_machine():
    Milk = 5000
    Coffee = 500
    Water = 2000
    total_earned = 0

    MENU = {
        "espresso": {"cost": 1.50,
                     "ingredients": {"Water": 50, "Coffee": 18}},
        "latte": {"cost": 2.50,
                  "ingredients": {"Milk": 150, "Water": 200, "Coffee": 24}},
        "cappuccino": {"cost": 3.50,
                       "ingredients": {"Milk": 100, "Water": 200, "Coffee": 24}},
    }

    resources = {"Milk": Milk,
                 "Coffee": Coffee,
                 "Water": Water}

    def is_resource_sufficient(order_ingredients):
        for item in order_ingredients:
            if resources[item] < order_ingredients[item]:
                print(f"Sorry, there is not enough {item}.")
                return False
        return True

    def process_coins():
        dollars = int(input("How many dollars? "))
        cents = int(input("How many cents? "))
        quarters = int(input("How many quarters? "))
        nickels = int(input("How many nickels? "))
        total = (dollars * 100 + cents + quarters * 25 + nickels * 5) / 100
        return total

    while True:
        print("\nWelcome to Coffee Machine!")
        choice = input("What would you like? (espresso/latte/cappuccino/no): ")
        choice = choice.lower()
        if choice == "no":
            break

        if choice not in MENU:
            print("Invalid selection. Please choose again.")
            continue

        drink = MENU[choice]
        if not is_resource_sufficient(drink["ingredients"]):
            continue

        print(f"The cost of {choice} is ${drink['cost']:.2f}")
        inserted = process_coins()

        if inserted < drink["cost"]:
            print("Sorry, that's not enough money. Money refunded.")
            continue

        change = round(inserted - drink["cost"], 2)
        if change > 0:
            print(f"Here is ${change:.2f} in change.")

        # Deduct resources
        for item in drink["ingredients"]:
            resources[item] -= drink["ingredients"][item]

        total_earned += drink["cost"]
        print(f"Here is your {choice}. Enjoy!")

    print("\nMachine shutting down...")
    print(f"Total earned: ${round(total_earned,2)}")
    print("Resources left:")
    for item in resources:
        print(f"{item}: {resources[item]}")
coffee_machine()