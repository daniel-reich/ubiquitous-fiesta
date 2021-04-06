
def min_swaps(s1, s2):
    different_digits = sum((1 for a, b in zip(s1, s2) if a != b))
    return different_digits / 2

