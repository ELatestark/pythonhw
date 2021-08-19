# !/usr/bin/env python3
# range through letters with given start and stop letters

def letters_range(letter1 : str, letter2 : str, step=1):
    return [chr(i) for i in range(ord(letter1), ord(letter2), step)]

print(letters_range("a", "a"))

print(letters_range("p", "g", -2))