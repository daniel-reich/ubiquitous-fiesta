
def repeating_cycle(n):
    res, first = 0, 1 % n * 10
    remainder, set_rem = first, set()
    while remainder not in set_rem:
        set_rem.add(remainder)
        res += 1
        remainder %= n
        remainder *= 10
    return res if remainder == first else -1

