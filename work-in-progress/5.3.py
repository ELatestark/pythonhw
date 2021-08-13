#!/usr/bin/env python3
from collections import Counter
from itertools import takewhile
userPrint=input('Insert some text and press Enter :\n').lower().split()
c = Counter(userPrint)
top=list(takewhile(lambda val: val[1] == c.most_common(1)[0][1], c.most_common()))
print('\n'.join("{} - {}".format(v, k) for k, v in top))