#!/usr/bin/env python3
# find all numbers and summarize them. there may be negative numbers in the string
import re
userInput = str(input('Insert any combination of digits, symbols and letters '))
sumI = re.findall('-?\d+', userInput)
sumI = list(map(int, sumI))
print(sum(sumI))