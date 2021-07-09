#!/usr/bin/python3
'''
Factorial sequence:

3! = 3 x 2 x 1

or,

5! = 5 x 4!
n! = n x (n-1)!

At the base case (When the recursion breaks), the return function will add up

'''

def factorial(n):
    if n == 0:
        # It will return 1 EVERY TIME the recursive function is called
        # Changing this return value results in unexpected behavior
        return 1
    else:
        return n * factorial(n-1)

n = 4
print(factorial(n))
