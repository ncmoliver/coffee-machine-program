from replit import clear
from menu import MENU

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_ingredient_available(ingredients):
    """Returns true if order can be made and false if ingredient is not available"""
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def process_coins():
    """Returns the total for the coins inserted"""
    print("Please insert coins")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """Return true if payment is accepted and false if insufficient"""
    if money_received >= drink_cost:
        clear()
        change = round(money_received - drink_cost, 2)
        print(f"Your Change ${change}\n")
        global profit
        profit += drink_cost
        return True
    else:
        print(f"Sorry there is not enough money. Amount refunded: ${money_received}")
        return False

def make_coffee(drink_name, ingredients):
    """Deduct the required ingredients from the resources"""
    for item in ingredients:
        resources[item] -= ingredients[item]

    print(f"Here is your {drink_name} ☕️\n"
          "Thank you for ordering.\nHave a Great Day!")

machine_pass = "1098"
machine_on = True

menu_selection = ("Welcome to Your Coffee Break!\n\n"
                  "Menu Selection\n"
                  "-----------------------\n"
                  "1. Espresso\n"
                  "2. Latte\n"
                  "3. Cappuccino\n"
                  "4. Exit")
admin_selection = ("Admin Screen\n"
                   "1. Generate Machine Status Report\n"
                   "2. Exit")

while machine_on:
    clear()
    print(menu_selection)
    choice = input("What would you like to drink? (Enter admin pass for admin menu): ")

    if choice == "4":
        machine_on = False
    elif choice == "1098":
        print(admin_selection)
        admin_choice = int(input("What would you like to perform? "))
        if admin_choice == 1:
            clear()
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${profit}")
            input("Press any key to return to the main menu...")
        else:
            print("Have a good day")
            machine_on = False
    elif choice in ["1", "2", "3"]:
        drink_map = {
            "1": "espresso",
            "2": "latte",
            "3": "cappuccino"
        }
        drink_name = drink_map[choice]
        drink = MENU[drink_name]
        if is_ingredient_available(drink["ingredients"]):
            clear()
            print("Customer Order Information")
            print("-" * 30)
            print(f"Customer Order: {drink_name}\nCost: ${drink['cost']}")
            print("-" * 30)
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(drink_name, drink["ingredients"])
                machine_on = False
    else:
        print("Error: Invalid option.")
