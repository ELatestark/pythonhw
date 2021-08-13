# !/usr/bin/env python3
#  remove duplicates from user input separated by whitespaces
userInput=input('Insert any combinations of text, numbers and symbols and press Enter\n').split()
print(set(userInput))
