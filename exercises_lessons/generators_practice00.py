#!/usr/bin/python

# Iterating through a generator:
gen1 = (a for a in range(3))
gen2 = (a for a in range(3))

for a in gen1:
    print(a)
print(f"Now it's empty: {list(gen1)}")

iterab = iter(gen2)     # generator
print(type(iterab))

# Same, now with lists:
l1 = [a for a in range(3)]

for a in l1:
    print(a)
print(f"Now it's not empty: {l1}")

iterab = iter(l1)       # List iterator
print(type(iterab))

