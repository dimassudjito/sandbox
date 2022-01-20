import random

def roll(quantity):
    result = random.randint(1,(quantity*6))
    return result

def main():
    menu = input("Ready to roll? Enter number of dice(s) or q to quit ")
    while menu.lower() != "q":

        is_int = True
        try:
            int(menu)
        except ValueError:
            is_int = False
        while not is_int:
            print('Invalid input')
            menu = input("Ready to roll? Enter number of dice(s) or q to quit ")
            is_int = True
            try:
                int(menu)
            except ValueError:
                is_int = False

        result = roll(int(menu))
        print(result)
        menu = input("Ready to roll? Enter number of dice(s) or q to quit ")

    print("Thanks for playing")

main()