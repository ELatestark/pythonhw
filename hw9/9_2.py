# !/usr/bin/env python3
# projecteuler problem 9. There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
print([(a*b*(a**2+b**2)**(1/2)) for a in range(501) for b in range(a) if 1000000-2000*a-2000*b+2*a*b==0][0])


