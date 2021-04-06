
def reversible_inclusive_list(start, end):
    a = start > end
    start, end = min(start, end), max(start, end)
    return sorted(list(range(start, end + 1)), reverse=a)

