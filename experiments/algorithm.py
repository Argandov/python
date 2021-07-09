#!/usr/bin/python3

'''

divide(n) is the same as log2(n)

Prints out the number of iterations it takes to split in half a number until
the end result is < 1. Useful for DSA coursework

'''

def divide(number):
    init_number = str(number)
    counter = 1
    while int(number) > 1:
        result = float(number/2)
        number = result
        counter += 1
    print(f"Iterations for {init_number}: {counter}")


num = input("Number: ")
# Take the input and do the tests with 3 halves of the same number
divide(int(num))
num = int(num)/2
divide(num)
num = int(num)/2
divide(num)
