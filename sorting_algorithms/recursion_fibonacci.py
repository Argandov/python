#!/usr/bin/python3

'''
find the Nth element in the fibonacci series
    
(0 and 1 are return values since they are the first elements of the series)
'''

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


z = 0
print(fibonacci(z))
z = 1
print(fibonacci(z))
z = 10
print(fibonacci(z))
