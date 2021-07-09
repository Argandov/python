from random import randint as ri
import time

intro = """
Welcome to Black Jack

This game generates a random number of cards for every deck.

note: the deck gets refreshed at every game.

"""

banner = "------------------------------"


def crupier_auto():
    print(intro)
    time.sleep(0.5)
    print(banner)
    games = int(input("How many random decks do you want to play? "))
    time.sleep(1)
    print("Good luck!")
    time.sleep(1)
    print(banner)
    nested_list = []
    # Generate X decks of Y number of cards (2 >= Y =< 7)
    for game in range(games):
        random_max = ri(2, 7)
        lg = [ri(1, 11) for card_numbers in range(random_max)]
        nested_list.append(lg)
    return nested_list
