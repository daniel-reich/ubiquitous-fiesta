
def chocolates_parcel(n_small, n_big, order):
    if 2 * n_small + 5 * n_big < order:
        return -1
    if order % 5 == 0 and order // 5 <= n_big:
        return 0
    big = 0 if n_big == 0 else min(n_big, order // 5)
    while big >= 0:
        small = (order - 5 * big) // 2
        if small <= n_small and 2 * small + 5 * big == order:
            return small
        big -= 1
    if order % 2 == 0 and order // 2 <= n_small:
        return order // 2
    return -1

