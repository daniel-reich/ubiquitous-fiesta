
def cycle_length(lst, n):
    lst_sorted, swaps = sorted(lst), 0
    current, target = lst.index(n), lst_sorted.index(n)
    while current != target:
        lst[current], lst[target] = lst[target], lst[current]
        swaps += 1
        target = lst_sorted.index(lst[current])
    return swaps

