#!/usr/bin/python3

''' 

Bubble sort algorithm from Mashrur class

i -> Index of element of list at comparison

O(n^2) Inconsistent?
'''


from random import randint

# from bubble_sort import bubble_sort

class Bubble_sort:
    def __init__(self, input_list):
        self.input_list = input_list
        sort_state = 0
        counter = 0
        print(f"[0] Sorting: {input_list}")
        while not sort_state:
            if Bubble_sort.swapper(input_list):
                sort_state = 1
                print(f"[S] Final list --- {input_list}")
            counter += 1

    def swapper(l1):
        swap_state = 0 
        for i in range(len(l1)-1):
            if l1[i] > l1[i+1]:
                l1[i], l1[i+1] = l1[i+1], l1[i] 
                print(f"  [+] Sorted --- {l1}")
                swap_state = 1 # Stays 0 if nothing to swap
        if swap_state == 0: # return 1 if the loops didn't change swap_state var
            return 1

# usage: Bubble_sort(list_to_sort)
