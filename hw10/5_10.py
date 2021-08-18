# !/usr/bin/env python3
# collatz hypothesis. print number of steps in which variable num become == 1
num = int(input('Input number :\n'))
count = 0
while num > 1:
    count += 1
    if num % 2 == 0:
        num /= 2
    else:
        num = num * 3 + 1
print(count)

