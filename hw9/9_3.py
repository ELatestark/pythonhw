# !/usr/bin/env python3
# problem 40. find value d[1]*d[10]*d[100]*d[1000]*d[10000]*d[100000]*d[1000000]
from functools import reduce

print(reduce(lambda init, x: init * x, [int(''.join(str(i) for i in range(1,1000001))[i-1]) for i in [pow(10, j) for j in range(0, 7)]]))