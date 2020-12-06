# OOP Coffee Machine
class CoffeeMachine:
    running = False

    def __init__(self, water, milk, coffee, money):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.money = money
        
        if not CoffeeMachine.running:
            self.start()

    def return_to_menu(self):
        print()
        self.start()

    def check_availability(self):
        self.not_available = ""
        if self.water - self.reduced[0] < 0:
            self.not_available = "water"
        elif self.milk - self.reduced[1] < 0:
            self.not_available = "milk"
        elif self.coffee - self.reduced[2] < 0:
            self.not_available = "coffee "

        if self.not_available != "":
            print(f"Sorry, not enough {self.not_available}!")
            return False
        else:
            print("I have enough resources, making you a coffee!")
            print("Please insert the coins......!")
            return True

    def deduct_supplies(self):
        self.water -= self.reduced[0]
        self.milk -= self.reduced[1]
        self.coffee -= self.reduced[2]
        self.money += self.reduced[3]

    def pay_amount(self):
        self.quarters = int(input("Quarters : "))
        self.dimes = int(input("Dimes : "))
        self.nickles = int(input("Nickles : "))
        self.pennies = int(input("Pennies : "))
        self.total = (self.quarters * 0.25) + (self.dimes * 0.10) + (self.nickles * 0.05) + (self.pennies * 0.01)
        # quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
        if (self.total == 2.5):
            print("Here is your " + self.choice + ". Enjoy! ")
            self.deduct_supplies()
        elif (self.total > 2.5):
            self.b = self.total - 2.5
            print("Here is your " + self.choice + ". Enjoy! ")
            print("Here is {:.2f} dollars in change".format(self.b))
            self.deduct_supplies()
        elif (self.total < 2.5):
            print("Sorry that's not the enough money. Money refunded!")

    def start(self):
        self.choice = input(
            "What do you want to buy? 1-espresso, 2-latte, 3-cappuccino, report, off :\n")
        if self.choice == '1':
            self.reduced = [100, 90, 25, 2.5]  
            if self.check_availability():  
                self.pay_amount()
                self.return_to_menu()
        elif self.choice == '2':
            self.reduced = [150, 100, 30, 3.5]
            if self.check_availability():
                self.pay_amount()
                self.return_to_menu()
        elif self.choice == "3":
            self.reduced = [200, 150, 20, 4]
            if self.check_availability():
                self.pay_amount()
                self.return_to_menu()

        elif self.choice == "report":
            print(f"The coffee machine has:")
            print(f"{self.water}ml of water")
            print(f"{self.milk}ml of milk")
            print(f"{self.coffee}g of coffee ")
            print(f"${self.money} of money")
            self.return_to_menu()

        elif self.choice == "off":
            return 0

CoffeeMachine(500, 350, 200,0)