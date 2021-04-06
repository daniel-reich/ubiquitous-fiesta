
def twins(lst):
    for i in range(1, len(lst)):
        if sum(lst[:i]) == sum(lst[i:]):
            return i

