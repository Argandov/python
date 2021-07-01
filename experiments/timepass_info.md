# Time-bound password

**This is only a thought experiment,** to see how it would be like to have a 2-dimensional password processing. An instant 2-factor authentication, with this 2 elements being "what you know" factors.

## How the idea works:
The main idea is to add the time factor to a plaintext password. After the first keystroke, a timer starts and ends just when the next keystroke hits and so on until "enter" is pressed. **BOTH** the password and the timers are stored as a code. 

In this way, the hash will be generated for a string, for example, "hey020", if the input was "h", then wait for <1 seconds + "e" + wait for 2 seconds + "y" + wait for <1 second. Obviously, "hey020" as an imput string wouldn't be valid, since the generated code would be "h0e0y0002000"

This is a potentially powerful authentication method, because, the time-factor is only known by the user, and the password itself is useless without the added time dimension.

## What this experiment could potentially solve:
- If properly implemented, it could make bruteforce attacks virtually impossible, by delaying each attempt by seconds and making the possible string matches exponentially bigger (As I'll explain later, for every possible word/phrase, the attempts are (string length)^t).
- "Shoulder surfing" or information leaks situations.
- Possibly keyloggers (Possibly, if properly designed).

## However, this code in particular is not (yet):
- A real authentication tool
- A real mechanism to secure data

## Usage:
- Introduce a password, and wait a certain time between letters. Since the timer is stored as an integer, any delay in a normal writing speed will be stored as 0, so 
don't worry about the speed, and type at a normal pace, but wait a certain amount of time when desired, to create a unique code.

## Posible security enhancements:
- Sandboxing; we don't want a Keylogger that can also register the time of the keystrokes. 

## Real world possible usage:
If an unwanted individual knows the password as a string, but doesn't know the time factor, it would still have a very low chance of getting it right. If the time factor becomes higher than 3 (seconds), it becomes impractical, so we can calculate the chances of getting it right:
  n = Password length in No. of characters
  t = time factor (Máx 3)
  n^t

**Example case:** Alice's password information was compromised by Bob, so he is trying to enter X service by using Alice's password. Even though the password is known by Bob, it would still take up to n^t attempts to access.

**Example case 2:** Let's bruteforce X service. Every single string combination gets multiplied by n^t, and every single attempt takes up a maximum of n*t seconds (t = 3). The number of attempts grows exponentially, and the time between each attempt grows by seconds. Just impossible :)

- Can you write down your password in a post-it and put it in your desk freely without risking anything? Possibly... But let's not do it. At least now.
