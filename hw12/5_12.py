# !/usr/bin/env python3
# collatz hypothesis. print number of steps in which variable num become == 1
p2=0
p1=1
n=int(input('Insert desired n-th Fibonacci number : \n'))
print(p2, p1, end=" ")
for i in range(n-1):
    curr=p2+p1
    print(curr, end=" ")
    p2=p1
    p1=curr

