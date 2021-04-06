
def iso_group(lst, c=float("-inf"), r = 1):
    if lst[0] == c: r += 1
    if lst[0] > c: c, r = lst[0], 1
    return iso_group(lst[1:],c,r) if lst[1:] else r*[c] if r-1 else c

