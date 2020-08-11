import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


def intro(villain):
    print_pause("You find yourself standing in an open field, filled with "
                "grass and yellow wildflowers.")
    print_pause(f"Rumor has it that {villain} is somewhere around "
                "here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty "
                "(but not very effective) dagger.\n")


def valid_input(prompt, options):
    while True:
        response = input(prompt).lower()
        for option in options:
            if response == option:
                return response
        print_pause("Sorry, try again")


def inField(weapons, villain):
    path = valid_input("Enter 1 to knock on the door of the house.\n"
                       "Enter 2 to peer into the cave.\n", ["1", "2"])
    if path == "1":
        inHouse(weapons, villain)
    if path == "2":
        inCave(weapons, villain)


def inHouse(weapons, villain):
    print_pause(f"This is {villain}'s hosue!\n"
                f"The {villain} attacks!")
    inHouse = valid_input("So c'mon and let me know, should you fight (1) "
                          "or should you go (2)?\n", ["1", "2"])
    if inHouse == "1":
        if "bazooka" in weapons:
            print_pause(f"You launch a granade and {villain} is gone!")
            weapons.remove("bazooka")
        else:
            print_pause("You're a karate master!")
            print_pause("Alas... it's of no help...")
            print_pause("You'll never be seen again :(")
        play_again()
    elif inHouse == "2":
        print_pause("Smart choise! Or maybe not? "
                    "Anyway you're out!\n")  # \n just for better readability
        inField(weapons, villain)


def inCave(weapons,villain):
    if "bazooka" in weapons:
        print_pause("Ooops, it wasn't the junkjard...")
        print_pause("And the entrance is locked now!")
        print_pause("You head out back to the field.\n")  # \n same as before
    else:
        print_pause("Uh-la-la! Weapons junkjard? With ammo!")
        print_pause("Tough choice...")
        print_pause("And you pick bazooka!")
        print_pause("Now we're talking! And you're out.\n")
        weapons.append("bazooka")
    inField(weapons, villain)


def play_again():
    print_pause("")
    play_again = valid_input("Wanna stay and play or wanna go?\nYes or No?\n",
                             ["yes", "no"])
    if play_again == "yes":
        print_pause("Great! Let's go!\n")
        time.sleep(1)
        playGame()
    elif play_again == "no":
        print_pause("See you next time!")


def playGame():
    weapons = []
    thugs = ['BadOne', 'WorseOne', 'WorstOne', 'Dreadful', 'Despikable']
    villain = random.choice(thugs)
    intro(villain)
    inField(weapons, villain)


playGame()
