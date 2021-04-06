
def reversible_inclusive_list(start, end):
    if start == end:
        return [end]
    elif start < end:
        return [start] + reversible_inclusive_list(start+1, end)
    else:
        return [start] + reversible_inclusive_list(start-1, end)

