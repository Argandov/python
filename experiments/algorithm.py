#!/usr/bin/python3
# Divides the input in half, and the result again in half until the end result is 1. To see how many iterations would take to split a given number, and how the count would grow as the numbers get bigger.

def divide(number):
    init_number = str(number)
    counter = 1
    while int(number) > 1:
        result = float(number/2)
        number = result
        counter += 1
    print(f"Iterations for {init_number}: {counter}")

divide(int(input("number: ")))
