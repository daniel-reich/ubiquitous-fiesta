
def largest_gap(lst):
    lst = sorted(lst)
    return max(
        n - lst[i]
        for i, n in enumerate(lst[1:])
    )

