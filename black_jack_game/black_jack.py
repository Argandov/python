#!/usr/bin/python3

import time
import crupier
from os import system

winner = "Your hand won!"
blackjack = "Black Jack!"
busted = "busted"

system("clear")

def black_jack(*args):
    total_sum = sum(list(args)[0])
    if total_sum < 21:
        print(f"Your hand is {total_sum}!\
 You're short on points!\n")
    elif total_sum > 21:
        for num in args[0]:
            if num == 11:
                total_sum -= 10
        if total_sum == 21:
            print(winner + "!!" + str(total_sum))
        elif total_sum < 21:
            print(f"Your hand is {total_sum}!\
 You're short on points!\n")
        elif total_sum > 21:
            print(f"{busted}! Your hand is {total_sum}!\n")
    elif total_sum == 21:
        if (len(list(args)[0])) > 2:
            print(winner)
        elif (len(list(args)[0])) == 2:
            print(blackjack)
            return 1


input("Press any key to start...")
gamifier = True

while True:
    for index, deck in enumerate(crupier.crupier_auto()):
        hand = ""
        print(f"\nGame no. {index + 1}: ")
        print("Your cards:")
        time.sleep(0.5)
        cards = "" 
        for card in deck:
            cards += str(card) + " "
            print(cards, end="\r")
            time.sleep(0.6)
        print(cards)
        if black_jack(deck) == 1:
            gamifier = False
            break
        time.sleep(2)
    if input("Again? y/n") == "n":
        break
