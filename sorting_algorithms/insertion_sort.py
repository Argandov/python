# from random import randint as r

'''
Insertion sort algorithm

starts at index 1 of a given list, compares its value backwards (index - 1).
if value[index] < value[index-1] begins swapping and comparing backwards again until index is 1,
and the loop continues at index 2
'''


def insertion_sort(arr):
    for key in range(1, len(arr)):   # Does not start from zero
        if arr[key] < arr[key-1]:   # Backwards comparison
            while key > 0 and arr[key] < arr[key-1]:
                arr[key], arr[key-1] = arr[key-1], arr[key]
                key -= 1
                print(f"[+] {arr}")


my_list = [4, 6, 2, 1, 7]
l2 = [a for a in my_list]  # Creating a second list, identical to l for comparison
print(f"[O] {my_list} Initial list ")
insertion_sort(my_list)
l2.sort()   # Using the built-in sort method and comparing to insertion_sort results
print(f"with sort function: {l2 == my_list}")
