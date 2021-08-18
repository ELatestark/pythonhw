# !/usr/bin/env python3
# projecteuler problem 9. There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
print([(a*b*c) for a in range(1001) for b in range(a) for c in range(b) if a*a == b*b + c*c and a+b+c==1000])

