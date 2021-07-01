#!/usr/bin/python3

# Bubble sort algorithm from Mashrur class

# O(n^2) Inconsistent?

from random import randint

def bubble_sort(l1):
    swap_state = 0 
    for i in range(len(l1)-1):
        if l1[i] > l1[i+1]:
            l1[i], l1[i+1] = l1[i+1], l1[i] 
            print(f"  [+] Sorted --- {l1}")
            swap_state = 1 # Stays 0 if nothing to swap
    if swap_state == 0: # return 1 if the loops didn't change swap_state var
        return 1

random_list = [randint(1,100) for num in range(1, 10)] # Random list of 10 numbers from 1-100
sort_state = 0
to_sort = random_list    # To quickly change input lists

print(f"[0] Sorting: {to_sort}")
while not sort_state:
    if bubble_sort(to_sort):
        sort_state = 1

print(f"[S] Final list --- {to_sort}")
