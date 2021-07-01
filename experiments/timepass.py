#! /usr/bin/env python

import time, hashlib
from pynput.keyboard import Key, Listener

password = ""
intervals = ""
count = "0"
a = ""
def on_press(key):
    global password
    global b
    global count
    b = time.time()
    if a:
        c = int(b - a)
        count += str(c)
    if key == Key.space:
        password += " "
    if key == Key.enter:
        # Stop listener
        code = hash_code(password, count)
        return False
    password += key.char

def hash_code(phrase, count):
    global hashed, compiled
    count = count[1:]
    compiled = phrase + count
    hashed_compiled = hashlib.sha256()
    hashed_compiled.update(compiled.encode())
    hashed = hashed_compiled.hexdigest()
    return hashed, compiled

def on_release(key):
    # print('{0} release'.format(key))
    global a
    a = time.time()

def listener():
    with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
            listener.join()

listener()

print(hashed + " de: " + compiled)

