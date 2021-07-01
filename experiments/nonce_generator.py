#!/usr/bin/python3

from Crypto.Hash import SHA256 as sha

# Generates a hash from <string>+<digit>, and the goal is to find
# what <digit> will hash the <string> with a resulting digest
# that starts with "666". From nonce in blockchain

h = sha.new()
count = 0
print(dir(h))
for digit in range(1, 1000000):
    h.update(b'Hello' + bytes(digit))

    if str(h.hexdigest()).lower().startswith("666"):
        print(str(h.decode("hex")))
        print(f"Nonce: {digit}\t@{count}\n")

        print(h.hexdigest())
    count += 1

# TO-DO: 
# Multi-threading vs. Multi-processing
