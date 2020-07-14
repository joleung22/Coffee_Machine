water = 400
milk = 540
beans = 120
cups = 9
money = 550


# parameters are set accordingly to the constants
def default(w, m, b, c, mon):
    print(f'The coffee machine has:\n'
          f'{w} ml of water\n'
          f'{m} ml of milk\n'
          f'{b} g of coffee beans\n'
          f'{c} of disposable cups\n'
          f'${mon} of money')


while True:
    action = input('Write action (buy, fill, take, remaining, exit):\n')
    if action == 'buy':
        buy = input(f'What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n')
        if buy != 1 and buy != 2 and buy != 3 and buy == 'back':
            print('Please choose from 1, 2, 3, Back to main menu!')
            print(action)
        elif buy == '1':
            if water > 0 and beans > 0 and cups > 0:
                if water < 250:
                    print('Sorry, not enough water!')
                elif beans < 16:
                    print('Sorry, not enough coffee beans!')
                elif cups < 1:
                    print('Sorry, not enough cups!')
                else:
                    water -= 250
                    beans -= 16
                    cups -= 1
                    money += 4
                    print('I have enough resources, making you a coffee!')
        elif buy == '2':
            if (water and milk and beans and cups) > 0:
                if water < 350:
                    print('Sorry, not enough water!')
                elif milk < 75:
                    print('Sorry, not enough milk!')
                elif beans < 20:
                    print('Sorry, not enough coffee beans!')
                elif cups < 1:
                    print('Sorry, not enough cups!')
                else:
                    water -= 350
                    milk -= 75
                    beans -= 20
                    cups -= 1
                    money += 7
                    print('I have enough resources, making you a coffee!')
        elif buy == '3':
            if water > 0 and milk > 0 and beans > 0 and cups > 0:
                if water < 200:
                    print('Sorry, not enough water!')
                elif milk < 100:
                    print('Sorry, not enough milk!')
                elif beans < 12:
                    print('Sorry, not enough coffee beans!')
                elif cups < 1:
                    print('Sorry, not enough cups!')
                else:
                    water -= 200
                    milk -= 100
                    beans -= 12
                    cups -= 1
                    money += 6
                    print('I have enough resources, making you a coffee!')
    elif action == 'fill':
        add_water = int(input('Write how many ml of water do you want to add:\n'))
        water += add_water
        add_milk = int(input('Write how many ml of milk do you want to add:\n'))
        milk += add_milk
        add_beans = int(input('Write how many grams of coffee beans do you want to add:\n'))
        beans += add_beans
        add_cups = int(input('Write how many disposable cups of coffee do you want to add:\n'))
        cups += add_cups
    elif action == 'take':
        print(f'I gave you ${money}\n')
        money = 0
    elif action == 'remaining':
        default(water, milk, beans, cups, money)
    elif action == 'exit':
        break
