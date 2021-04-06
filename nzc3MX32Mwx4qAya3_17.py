
def ranged_reversal(lst, start, finish):
    lst1 = list(reversed(lst[start:finish+1]))
    del lst[start:finish+1]
    return lst[:start] + lst1 + lst[start:]

