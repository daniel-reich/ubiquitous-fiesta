
def twins(lst):
    for i in range(len(lst)):
        if sum(lst[:i])==sum(lst[i:]):return i

