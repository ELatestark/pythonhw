# !/usr/bin/env python3
counter = 0
def isDecAndBinPalindrome(number : int) -> bool:
    isDecPal, isBinPal = isStrPal(str(number)), isStrPal(str("{0:b}".format(number)))
    return isDecPal and isBinPal

def isStrPal(string : str) -> bool:
    return string == string[::-1]


for i in range(1000000):
    if isDecAndBinPalindrome(i):
        counter+=i
print(counter)
