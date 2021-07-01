#!/usr/bin/python3

from random import randint

'''

Selection sort algorithm from Mashrur class

x -> Index of first element at comparison
y -> Index of second element at comparison

2 loops:

compare & swap:
    when x = 0
    l1[x] & l1[y++]

compare & swap:
    when x = 1
    l1[x] & l1[y++] (y always > x)

'''
# Random list generator (10 numbers from 1-100):
l1 = [randint(1,100) for num in range(1, 10)] 

def sel_sort(l1):
    swap_state = 0 
    x = 0
    while x < len(l1):
        for y in range(x, len(l1)-1): 
        # The y index MUST be greater than x
        # else, the sorting runs also backwards
            if l1[x] > l1[y+1]:
                l1[x], l1[y+1] = l1[y+1], l1[x] 
                # Print the new list every time a swap happens:
                print(f"  [+] Sorted --- {l1}")
                swap_state = 1 # Stays 0 if nothing to swap
        x += 1
        if swap_state == 0: # return 1 if the loops didn't change swap_state var
            return 1

print(f"[0] Sorting: {l1}")
while not sort_state:
    if sel_sort(l1):
        sort_state = 1
        print(f"[S] Final list --- {l1}")

