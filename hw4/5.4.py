#!/usr/bin/env python3
import re
userInput = str(input('Insert any combination of digits, symbols and letters '))
sumI = re.findall('-?\d+', userInput)
sumI = list(map(int, sumI))
print(sum(sumI))