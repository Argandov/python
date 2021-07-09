#!/usr/bin/python3

'''

Mindfuck using recursion (Useless function)

'''


def br(n):
    print(n)
    if n == 0:
        return 1
    elif n == 5:
        return 1
    else:
        return n*br(n-1) + br(5)

print(f"recursive: {br(4)}")
