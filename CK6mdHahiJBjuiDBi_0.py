
def can_fit(w, b):
    w.sort(reverse=True)
    count = 0
    while w:
        count += 1
        fill = w[0]
        w = w[1:]
        idx = 0
        while fill < 10 and idx < len(w):
            if w[idx] <= 10 - fill:
                fill += w[idx]
                w = w[:idx] + w[idx + 1:]
            else:
                idx += 1
    return count <= b

