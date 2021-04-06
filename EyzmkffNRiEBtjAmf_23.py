
def does_brick_fit(b1, b2, b3, w, h) -> bool:
    t1 = tuple(sorted([b1, b2, b3]))[:2]
    return max(w,h) >= max(t1) and min(w, h) >= min(t1)

