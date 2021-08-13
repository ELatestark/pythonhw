# !/usr/bin/env python3
# print most common word and its quantity
def word_count(str):
    counts = dict()
    words = str.lower().split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

user_string = word_count(input())
max_value = max(user_string.values())
output=[k for k,v in user_string.items() if v == max_value]
for i in range(len(output)):
    print(max_value, '-', output[i])
