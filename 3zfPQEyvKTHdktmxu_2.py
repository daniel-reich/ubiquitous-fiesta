
def big_sub(lst):
    best, current, start, beststart, end = 0, 0, 0, 0, 0
    for y, x in enumerate(lst):
        current = max(0, current + x)
        if current == 0:
            start = y + 1
        if current >= best:
            best = current
            end = y
            beststart = start
    return [best, beststart, end]

