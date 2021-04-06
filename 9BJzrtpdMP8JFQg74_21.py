
def twins(lst):
    for i in range(0,len(lst)):
        if sum(lst[:i]) == sum(lst[i:]):
            return i

