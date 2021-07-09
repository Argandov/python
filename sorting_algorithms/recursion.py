#!/usr/bin/python3

def counter(n):
    if n == 0:
        return "yay"
    else:
        return counter(n-1)
print(counter(1))
