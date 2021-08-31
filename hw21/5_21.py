# !/usr/bin/env python3
# define function to merge two iterators
def merge(first_iterator, second_iterator):
    current_iter1 = next(first_iterator)
    current_iter2 = next(second_iterator)
    while True:
        if current_iter1 <= current_iter2:
            yield current_iter1
            try:
                current_iter1 = next(first_iterator)
            except StopIteration:
                while True:
                    yield current_iter2
                    try:
                        current_iter2 = next(second_iterator)
                    except StopIteration:
                        return
        else:
            yield current_iter2
            try:
                current_iter2 = next(second_iterator)
            except StopIteration:
                while True:
                    yield current_iter1
                    try:
                        current_iter1 = next(first_iterator)
                    except StopIteration:
                        return


print(list(merge((x for x in range(1, 4)), (x for x in range(2, 5)))))