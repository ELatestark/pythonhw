# !/usr/bin/env python3
user_input=input().split()
list_from_input=results = list(map(int, user_input))
print(list_from_input)
for i in range(1, max(list_from_input)+2):
    if i not in list_from_input:
        break
print(i)

