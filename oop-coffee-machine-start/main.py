from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

while True:
    choice = input(f'What would you like? ({menu.get_items()}): ')
    if choice == 'report':
        coffee_maker.report()
        money_machine.report()
    elif choice == 'off':
        break
    else:
        order = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(order):
            money_machine.make_payment(order.cost)
            coffee_maker.make_coffee(order)
