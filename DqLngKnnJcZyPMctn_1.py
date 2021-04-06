
def stock_picker(lst):
    best = - 1
    for i in range(len(lst) - 1):
        if lst[i] < max(lst[i + 1:]):
            c = max(lst[i + 1:])
            best = max(best, c - lst[i])
    return best

