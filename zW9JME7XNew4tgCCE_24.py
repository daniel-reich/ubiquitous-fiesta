
def reversible_inclusive_list(beg, end):
    if beg > end:
        return list(range(beg, end-1, -1))
    return list(range(beg, end+1))

