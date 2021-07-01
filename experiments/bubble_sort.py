#!/usr/bin/python3

# Bubble sort algorithm from Mashrur class

# Entonces, O(n^2) A qué es igual?

def bubble_sort(l1):
    swap_state = 0 
    for i in range(len(l1)-1):
        if l1[i] > l1[i+1]:
            l1[i], l1[i+1] = l1[i+1], l1[i] 
            print(f"  [+] Sorted --- {l1}")
            swap_state = 1 # Stays 0 if nothing to swap
    if swap_state == 0: # return 1 if the loops didn't change swap_state var
        return 1

 
l1 = [2, 1, 4, 3, 2]
l2 = [34, 1, 2, 4, 3, 3, 5, 8, 87, 62, 68, 6, 52, 356, 78,\
        876, 2, 45, 52, 2345, 6, 2, 1, 2, 7, 2, 1, 234, 7, 21, 23, 45]
sort_state = 0
to_sort = l2    # To quickly change input lists
print(f"[0] Sorting: {to_sort}")
while not sort_state:
    if bubble_sort(to_sort):
        sort_state = 1

print(f"[S] Final list --- {to_sort}")
