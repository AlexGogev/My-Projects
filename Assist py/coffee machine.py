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
  
 }


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

penny = 0.01
dime = 0.10
nickel = 0.05
quarter = 0.25


def report():
    for k,v in resources.items():
        print(k,v)


expresso_water = MENU["espresso"]["ingredients"]["water"]
expresso_coffee = MENU["espresso"]["ingredients"]["coffee"]
expresso_price = MENU["espresso"]["cost"]



latte_water = MENU["latte"]["ingredients"]["water"]
latte_coffee = MENU["latte"]["ingredients"]["coffee"]
latte_price = MENU["latte"]["cost"]


def start():
    choice = input("What would you like? (Expresso - 1, Capoccino - 2, or report: ")
    if choice == "report":
        report()
        return start()

    if choice == "1":
        avl_water = resources["water"] = resources["water"] - expresso_water
        avl_coffee = resources["coffee"] = resources["coffee"] - expresso_coffee
        print(f"remaining water {avl_water}ml")
        print(f'remaining coffee {avl_coffee}ml')
        
        if avl_water <= 0 or avl_coffee <= 0:    
            print("no resources in machine")
            recharged = input("machine topped up? ")
            if recharged == "yes":
                resources["water"] = 300
                resources["coffee"] = 100
                start()
            else:
                print("You need to regarche water and coffe...")
                
        else:
            print("please insert coins")
            money = []
            penny = float(input(f"how many peny: " ))
            money.append(penny * 0.01) 
            dime = float(input(f"how many dime: " ))
            money.append(dime * 0.1) 
            nickel = float(input("how many nickels: ")) 
            money.append(nickel * 0.05)
            quarter = float(input("how many quarter: ")) 
            money.append(quarter * 0.25)
            

            total = sum(money)
            if total < expresso_price:
                print(f"insuficient price. You have {total} but price is {expresso_price}")
                report()
                return start()
            else:
                print(f'enjoy! dont forget your cgange {expresso_price - total}')
                report()
                return start()


    elif choice == "2":
        avl_water = resources["water"] = resources["water"] - latte_water
        avl_coffee = resources["coffee"] = resources["coffee"] - latte_coffee
        print(f"remaining water {avl_water}ml")
        print(f'remaining coffee {avl_coffee}ml')
        
        if avl_water <= 0 or avl_coffee <= 0:    
            print("no resources in machine")
            recharged = input("machine topped up? ")
            if recharged == "yes":
                resources["water"] = 300
                resources["coffee"] = 100
                start()
                
            else:
                print("You need to regarche water and coffe...")
                
        else:
            print("please insert coins")
            money = []
            penny = float(input(f"how many peny: " ))
            money.append(penny * 0.01) 
            dime = float(input(f"how many dime: " ))
            money.append(dime * 0.1) 
            nickel = float(input("how many nickels: ")) 
            money.append(nickel * 0.05)
            quarter = float(input("how many quarter: ")) 
            money.append(quarter * 0.25)
            

            total = sum(money)
            if total < expresso_price:
                print(f"insuficient price. You have {total} but price is {expresso_price}")
                report()
                return start()
            else:
                print(f'enjoy! dont forget your cgange {expresso_price - total}')
                report()
                return start()

start()
            

