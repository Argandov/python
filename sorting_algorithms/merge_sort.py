#!/usr/bin/python3

from random import randint as r


def merge_sorted(l1, l2):
    sorted_arr = []
    i, j = 0, 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            sorted_arr.append(l1[i])
            i += 1
        else:
            sorted_arr.append(l2[j])
            j += 1
    # Append the remaining elements in case l1/l2 are of diff len()
    while i < len(l1):
        sorted_arr.append(l1[i])
        i += 1
    while j < len(l2):
        sorted_arr.append(l2[j])
        j += 1
    return sorted_arr


# Case 1
l2 = [1, 3, 5, 7, 9, 999999]
l1 = [2, 4, 6, 8, 10, 100, 1000, 20000]
print(f"Case 1: Merged list: {merge_sorted(l1, l2)}")

''' [Not yet ready for random lists]
# Case 2: Random lists
l1 = [r(1, 20) for a in range(20)]
l2 = [r(1, 20) for a in range(20)]
print(f"Case 2: Random lists - Lists:\n{l1}\n{l2}")
print(f"\tMerged list: {merge_sorted(l1, l2)}")
'''
