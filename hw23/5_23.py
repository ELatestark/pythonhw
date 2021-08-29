#!/usr/bin/env python3
# return n-dimensional array based on arguments of function

def n_arr(sizes, value=""):
    if (len(sizes) == 1):
        return [value] * sizes[0]
    else:
        return [n_arr(sizes[1:], value) for i in range(sizes[0])]

matrix = n_arr([2,2])
print(matrix)
matrix = n_arr([2,2,2])
print(matrix)