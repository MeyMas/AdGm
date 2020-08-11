import time
import random
weapons = []


def print_pause(message):
    print(message)
    time.sleep(1)


def valid_input(prompt, options):
    while True:
        response = input(prompt).lower()
        for option in options:
            if option in response:
                return response
        print("Sorry, try again")


while True:
    thugs = ['BadOne', 'WorseOne', 'WorstOne', 'Dreadful', 'Despikable']
    villain = random.choice(thugs)

    print_pause("You find yourself standing in an open field, filled with "
                "grass and yellow wildflowers.")
    print_pause(f"Rumor has it that {villain} is somewhere around "
                "here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective) "
                "dagger.\n")
    while True:
        path = input("Enter 1 to knock on the door of the house.\n"
                     "Enter 2 to peer into the cave.\n").lower()
        if path == "1":
            while True:
                print_pause(f"This is {villain}'s house!\n"
                            f"The {villain} attacks!")
                inHouse = input("So c'mon and let me know, should I fight (1) "
                                "or should I go (2)?\n")
                if inHouse == "1":
                    if "bazooka" in weapons:
                        print_pause(f"You launch a granade and {villain} "
                                     "is gone!")
                        weapons.remove("bazooka")
                        break
                    else:
                        print_pause("You're a karate master!")
                        print_pause("Alas... it's of no help...")
                        print_pause("You'll never be seen again :(")
                        break
                elif inHouse == "2":
                    print_pause("Smart choise! Or maybe not? "
                                "Anyway you're out!\n")
                    break
                else:
                    print_pause("Sorry, try again.")
            if inHouse == "1":
                break
        elif path == "2":
            if "bazooka" in weapons:
                print_pause("Ooops, it wasn't the junkjard...")
                print_pause("And the entrance is locked now!")
                print_pause("You head out back to the field.\n")
            else:
                print_pause("Uh-la-la! Weapons junkjard? With ammo!")
                print_pause("Tough choice...")
                print_pause("And you pick bazooka!")
                print_pause("Now we're talking! And you're out.\n")
                weapons.append("bazooka")
        else:
            print_pause("Sorry. It looks like you're confused.")
    while True:
        print_pause("")
        play_again = input("Wanna stay and play or wanna go? "
                           "'yes' or 'no'?\n").lower()
        if "yes" in play_again:
            print_pause("Great! Let's go!")
            time.sleep(1)
            break
        elif "no" in play_again:
            print_pause("See you next time!")
            time.sleep(1)
            break
        else:
            print_pause("Sorry, try again.")
            time.sleep(1)
    if "no" in play_again:
        break
