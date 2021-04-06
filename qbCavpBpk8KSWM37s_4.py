
def largest_gap(lst):
    lst = sorted(lst)
    count = 0
    for i, v in enumerate(lst[:-1]):
        if lst[i + 1] - lst[i] > count:
            count = lst[i + 1] - lst[i]
    return count

