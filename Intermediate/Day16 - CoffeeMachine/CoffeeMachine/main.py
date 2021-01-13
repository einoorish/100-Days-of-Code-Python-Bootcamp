import data

isOn = True


def print_report():
    print(f"Water: {data.resources['water']}ml")
    print(f"Milk: {data.resources['milk']}ml")
    print(f"Coffee: {data.resources['coffee']}g")
    print(f"Money: ${data.resources['money']}")


def is_sufficient_resources(ingredients):
    for item in ingredients:
        if ingredients[item] > data.resources[item]:
            print(f"Sorry, there's not enough {item}")
            return False
    return True


def process_coins(cost):
    """Returns the total calculated from coins inserted"""
    # quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01

    print(f"The price is {cost}. Please, insert coins.")
    total = int(input("quarters: ")) * 0.25
    total += int(input("dimes: ")) * 0.1
    total += int(input("nickles: ")) * 0.05
    total += int(input("pennies: ")) * 0.01
    return total


def is_transaction_successful(inserted_money, price):
    if inserted_money < price:
        print("Sorry that's not enough money. Money refunded.")
        return False

    if inserted_money > price:
        change = round(inserted_money - price, 2)
        print(f"Here is ${change} in change.")

    data.resources["money"] += price
    return True


def make_coffee(drink_name, ingredients):
    for item in ingredients:
        data.resources[item] -= ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


while isOn:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        isOn = False
    elif choice == "report":
        print_report()
    else:
        if choice in data.MENU:
            drink = data.MENU[choice]
            if is_sufficient_resources(drink["ingredients"]):
                inserted_money = process_coins(drink["cost"])
                if is_transaction_successful(inserted_money, drink["cost"]):
                    make_coffee(choice, drink["ingredients"])
