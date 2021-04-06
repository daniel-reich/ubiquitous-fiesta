
def number_of_swaps(lst):
    if sorted(lst) == lst:
        return 0
    swaps = 0
    while lst != sorted(lst):
        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                lst = lst[:i] + [lst[i+1]] + [lst[i]] + lst[i+2:]
                swaps += 1
    return swaps

