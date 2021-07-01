from random import randint,choice
from string import ascii_lowercase

'''
Random & List comprehension exercise
'''

my_list = [randint(0,100) for num in range(22)]
my_list = []


# Es lo mismo que:
for num in range(22):
    num = randint(0,100)
    my_list.append(num)

# Usando choice:
l1 = ['apples','pears','bananas']
print(choice(l1))



