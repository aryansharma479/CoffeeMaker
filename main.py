from menu import Menu, MenuItem
from coffeemaker import CoffeeMaker
from machine import MoneyMachine

money_machine = MoneyMachine()
money_machine.report()
coffeemaker = CoffeeMaker()
menu = Menu()
is_on = True
while is_on:
  options = menu.get_items()
  choice = input(f"What do you want to choose? {options} or report:")
  if choice == "off":
    is_on = False
  elif choice == 'report':
    coffeemaker.report()
    money_machine.report()
  else:
    drink = menu.find_drink(choice)
    if coffeemaker.is_resource_sufficient(
        drink) and money_machine.make_payment(drink.cost):
      coffeemaker.make_coffee(drink)
