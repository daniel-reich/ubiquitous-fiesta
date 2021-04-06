
def largest_gap(lst):
    lg, lst = 0, sorted(lst)
    for i in range(len(lst) - 1):
        diff = lst[i + 1] - lst[i]
        if diff > lg:
            lg = diff
    return lg

