#!/usr/bin/python3

from Crypto.Hash import SHA256 as sha

# Generates a hash from <string>+<digit>, and the goal is to find
# what (nonce) will result in a hash that starts with "666". 
# (From nonces in blockchain)

h = sha.new()
count = 0
print(dir(h))
for digit in range(1, 1000000):
    h.update(b'This string can be of any data' + bytes(digit))

    if str(h.hexdigest()).startswith("666"):
        print(str(h.decode("hex")))
        print(f"Nonce found: {digit}\t@{count} iteration\n")
        print(h.hexdigest())
    count += 1

# TO-DO: 
# Multi-threading vs. Multi-processing
