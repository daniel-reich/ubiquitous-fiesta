
def largest_gap(lst):
    l = sorted(lst)
    return max(abs(l[i] - l[i + 1]) for i, _ in enumerate(l[:-1]))

