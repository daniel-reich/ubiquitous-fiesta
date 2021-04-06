
def is_consecutive(s, size=None):
    if size is None:
        size = 1
    len_s = len(s)
    if not len_s % size:
        lst = [int(s[k * size: (k + 1) * size]) for k in range(len(s) // size)]
        if (all(a + 1 == b for a, b in zip(lst, lst[1:])) or
                all(a - 1 == b for a, b in zip(lst, lst[1:]))):
            return True
    return is_consecutive(s, size + 1) if size <= len_s / 2 else False

